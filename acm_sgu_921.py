FIN = open('input.txt','r')
FOUT = open('output.txt','w')
InputData = FIN.read().split()
a, b = map(int,InputData)
if a > 0:
    FOUT.write('1')
elif a < 0:
    if b % 2 == 1:
        FOUT.write('-1')
    else:
        FOUT.write('1')
elif a == 0:
    FOUT.write('0')
FIN.close()
FOUT.close()
