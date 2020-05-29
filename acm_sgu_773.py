FIN = open('input.txt','r')
FOUT = open('output.txt','w')
InputData = FIN.read().split()
m, t = int(InputData[0]), int(InputData[1])
c = 0
while t < m:
    t = t * 2
    c += 1
FOUT.write(str(c))
FIN.close()
FOUT.close()


