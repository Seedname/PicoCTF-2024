import struct
with open('endianness-v2/challengefile', 'rb') as f:
    integer = 4292411360
    hexad = hex(integer)[2:]   
    # print(hexad[:2]) 
    output = ""
    for i in range(0, len(hexad), 2):
        output += chr(int(hexad[i:i+2], 16))
    print(output)
    # text = bytearray(f.read(4))
    # print(text)
    # integer = int(text.hex(), 16)
    # print(integer)
    # #4292411360
    # little_endian = int(text.hex()[::-1], 16)
    # # little_endian = struct.pack('<I', integer)
    # print(little_endian)
    # # print(text)
    # small = little_endian(text).hex()
    # small = text[229:1258][::-1]
    # print(chr(small[0]))
    # output = ''.join([chr(byte) for byte in small])
    # print(output)
    # # print(small.hex())
    # output = ""
    # for i in range(0, len(small), 2):
        # subset = chr(int(small[i:i+2], 16))
        # output += subset
    # print(output)
    # search_term = bytearray("{", encoding="UTF-8")[::-1]
    # if search_term in text:
    #     print(text.index(search_term))

    # search_term = bytearray("}", encoding="UTF-8")[::-1]
    # if search_term in text:
    #     print(text.index(search_term))

    
    # print(output)