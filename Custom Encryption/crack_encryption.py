def dynamic_xor_decrypt(encrypted, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(encrypted[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def generator(g, x, p):
    return pow(g, x) % p

def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True

def decrypt(encrypted, key):
    cipher = []
    for value in encrypted:
        cipher.append(chr(value//(key*311)))
    return ''.join(cipher)

def test(semi_cipher, a, b):
    ps = [97]
    gs = [31]   
    # ps = [i for i in range(2, 100) if is_prime(i)]
    # gs = [i for i in range(2, 100) if is_prime(i)]
    print(len(ps) * len(gs))
    all_decrypted = []
    for p in ps:
        for g in gs:
            u = generator(g, a, p)
            v = generator(g, b, p)
            key = generator(v, a, p)
            b_key = generator(u, b, p)
            shared_key = None
            if key == b_key:
                shared_key = key
            else:
                # print("Invalid key")
                continue
            if shared_key == 0:
                continue
            decrypted = decrypt(semi_cipher, shared_key)[::-1]
            final = dynamic_xor_decrypt(decrypted, "trudeau")[::-1]
            all_decrypted.append(final)
            print(final)
            if "pico" in final:
                print(final)
    return final

semi_cipher = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
a = 94
b = 29
decrypted = test(semi_cipher, a, b)

# print(decrypted)

