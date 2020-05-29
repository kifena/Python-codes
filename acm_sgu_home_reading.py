FIN  = open('input.txt',  'r')
FOUT = open('output.txt', 'w')
InputData = FIN.read().split()
n, m = map(int,InputData)
if (n) % (m) > 0:
    FOUT.write (str(n //m + 1))
else:
    FOUT.write (str(n // m))
FOUT.close()
FIN.close()
