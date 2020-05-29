FIN = open('input.txt','r')
FOUT = open('output.txt','w')
m = FIN.read()
n = int(m)
c = ''
if n == 0:
    c = str(n)
else:
    while n > 0:
        c = str(n % 2) + c
        n //= 2
FOUT.write(c)
FIN.close()
FOUT.close()
