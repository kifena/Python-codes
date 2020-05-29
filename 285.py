FIN = open('input.txt','r')
FOUT = open('output.txt','w')
InputData = FIN.read().split()
A, B = int(InputData[0]),int(InputData[1])
if B > A:
    FOUT.write(str(A + 1))
else:
    FOUT.write(str(A - 1))
FIN.close()
FOUT.close()
