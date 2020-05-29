FIN = open('input.txt','r')
FOUT = open('output.txt','w')
n = int(FIN.read())
i = 0
while n > 0:
    if n % 2 == 1:
        i += 1
    n //= 2
FOUT.write(str(i))
FIN.close()
FOUT.close()
