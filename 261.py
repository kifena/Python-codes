import math
FIN = open('input.txt','r')
FOUT = open('output.txt','w')
InputData = FIN.read().split()
a, b = float(InputData[0]), float(InputData[1])
F1 = (a + b) / 2
F2 = math.sqrt(a * b)
ans = math.sqrt(F1 * F2)
FOUT.write(str(round(ans,2)))
FIN.close()
FOUT.close()
