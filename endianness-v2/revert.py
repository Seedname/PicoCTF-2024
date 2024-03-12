def find_little_endian(word):
    little_endian = ["" for _ in range(len(word))]
    for i in range(len(word)):
        little_endian[len(word)-i-1] = hex(ord(word[i]))[2:].upper()
    return ''.join(little_endian)

def find_big_endian(word):
    little_endian = ["" for _ in range(len(word))]
    for i in range(len(word)):
        little_endian[i] = hex(ord(word[i]))[2:].upper()
    return ''.join(little_endian)
    
print(find_little_endian("pzuyh"))
print(find_big_endian("pzuyh"))