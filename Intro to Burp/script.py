with open('Intro to Burp/out.txt', 'w') as f:
    for i in range(10**6):
        f.write(str(i).zfill(6) + "\n")