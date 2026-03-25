import struct

c = [[b'\xc8',b'\xce',b'\xc5',b'\x06'],
     [b'\xc8',b'\xce',b'\xc5',b'\x06'],
     [b'\xc8',b'\xce',b'\xc5',b'\x06'],
     [b'\xc8',b'\xce',b'\xc5',b'\x06'],
     [b'\xcc',b'\xce',b'\xc5',b'\x06']]


sum = 0

for i in range(5):
    temp = b''
    for j in range(4):
        temp += ord(c[i][j]).to_bytes(1)
        print(temp)
    sum += int.from_bytes(temp, byteorder='little')


print(hex(sum))
