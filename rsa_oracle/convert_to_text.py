def encode(ciphertext):
    return ciphertext * 873224563026311790736191809393138825971072101706285228102516279725246082824238887755080848591049817640245481028953722926586046994669540835757705139131212

def decode(int_output):
    int_output //= 32
    hex_out = hex(int_output)[2:]
    bytes = bytearray.fromhex(hex_out)
    return bytes.decode('utf-8')

# print(encode(3970921715843088939034957324911350626212240950470862928977787663977406608468604142079377234654007309935996972791790270166961305129444105909465676647301056))
# print(decode(int("7264c86a660", 16)))
# password = 92d53
