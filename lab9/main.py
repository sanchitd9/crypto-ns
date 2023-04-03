f1 = open('out64_1.bin', 'rb')
f2 = open('out64_2.bin', 'rb')

data1 = f1.read()
data2 = f2.read()

l1 = list()
l2 = list()

for item in data1:
    l1.append(hex(item))

for item in data2:
    l2.append(hex(item))

print("out64_1.bin   |   out64_2.bin")
print("------------------------------")
for i in range(len(l1)):
    if l1[i] != l2[i]:
        print(str(l1[i]) + "\t      |\t  " + str(l2[i]))

f1.close()
f2.close()