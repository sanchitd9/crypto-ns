#!/usr/bin/bash

# Compile the source code
gcc benign_evil.c -Wall

# Extract the prefix
head -c 12352 a.out > prefix

# Create the collision files
md5collgen -p prefix -o out1.bin out2.bin

echo -e

# Check that they are different
diff out1.bin out2.bin

echo -e

# Check that they have the same hash
md5sum out1.bin out2.bin

# Extract the suffix
tail -c +12481 a.out > suffix

# Extract P and Q
tail -c 128 out1.bin > P
tail -c 128 out2.bin > Q

# Extract suffix1 and suffix2 from the suffix
head -c 288 suffix > suffix1
tail -c +417 suffix > suffix2

# Create the two binaries
cat prefix P suffix1 P suffix2 > a1.out
cat prefix Q suffix1 P suffix2 > a2.out

echo -e
chmod 764 a1.out a2.out

# Execute the binaries
./a1.out

echo -e

./a2.out

echo -e

md5sum a1.out a2.out

