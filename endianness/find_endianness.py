def find_little_endian(word):
    return bytes(word[::-1], 'utf-8').hex().upper()

def find_big_endian(word):
    return bytes(word, 'utf-8').hex().upper()
    
print(find_little_endian("pzuyh"))
print(find_big_endian("pzuyh"))