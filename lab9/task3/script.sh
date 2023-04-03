#!/usr/bin/bash

gcc print_array.c -Wall

head -c 12352 a.out > prefix

md5collgen -p prefix -o out1.bin out2.bin

echo -e "\n"

tail -c +12353 a.out > suffix

tail -c 128 out1.bin > P
tail -c 128 out2.bin > Q

cat prefix P suffix > a1.out
cat prefix Q suffix > a2.out

chmod 764 a1.out a2.out

echo -e "\nDiff of the final output files:"
diff a1.out a2.out

echo -e

echo -e "\nMD5 hashes of the output files:"
md5sum a1.out a2.out

echo -e "\nOutput of program 1\n"

./a1.out

echo -e "\nOutput of program 2\n"

./a2.out
