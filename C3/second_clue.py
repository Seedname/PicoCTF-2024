#asciiorder
#fortychars
#selfinput
#pythontwo

chars = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
# from fileinput import input
# for line in input():
    # chars += line
b = 1
out = ""
for i in range(len(chars)):
    if i == b**3:
        out += chars[i]
        b += 1
    
print(out)