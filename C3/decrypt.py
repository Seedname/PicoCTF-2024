out = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

prev = 0
chars = ""
for enc in out:
    cur = (lookup2.index(enc) + prev) % 40
    chars += lookup1[cur]
    prev = cur

print(chars)

# got from the second clue
b = 1
out = ""
for i in range(len(chars)):
    if i == b**3:
        out += chars[i]
        b += 1
    
print("Flag: picoCTF{"+ out + "}")