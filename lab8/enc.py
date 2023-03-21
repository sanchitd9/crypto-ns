#!/usr/bin/python3

import sys
from Crypto.Cipher import AES
from Crypto.Util import Padding

keys_file = sys.argv[1]

with open(keys_file, "r") as f:
    possible_keys = [x.strip() for x in f.readlines()]
    for i in range(len(possible_keys)):
        possible_keys[i] = possible_keys[i] + ("#" * (16 - len(possible_keys[i])))

data = b'This is a top secret.'
print("Length of data: {0:d}".format(len(data)))

expected_ciphertext = '3879c71b232cd0d2fc6f5ffcc1d76f074c0fcbe007d9cc53939fdeebf1d6ffd2'
print("Expected ciphertext: {0}".format(expected_ciphertext))
print("--------------------------------------------------------------------------------")

iv_hex_string  = 'aabbccddeeff00998877665544332211'
iv  = bytes.fromhex(iv_hex_string)

for key in possible_keys:
    key_string = key
    key = bytes.fromhex(key.encode('utf-8').hex())
    # Encrypt the entire data
    cipher = AES.new(key, AES.MODE_CBC, iv)                   
    ciphertext = cipher.encrypt(Padding.pad(data, 16))

    if ciphertext == bytes.fromhex(expected_ciphertext):
        print("MATCH!")
        print(key_string)
        break


