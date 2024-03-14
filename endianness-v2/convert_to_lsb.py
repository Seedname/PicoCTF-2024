with open('endianness-v2/challengefile', 'rb') as f:
    bytedata = bytearray(f.read())
    new_bytedata = bytearray()

    for i in range(0, len(bytedata), 4):
        thirty_two_bit_substring = bytedata[i:i+4][::-1]
        new_bytedata.extend(thirty_two_bit_substring)
    
    with open('endianness-v2/challengefile_reversed', 'wb') as g:
        g.write(bytes(new_bytedata))