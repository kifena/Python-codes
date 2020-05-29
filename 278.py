FIN = open('input.txt','r')
FOUT = open('output.txt','w')
InputData = FIN.read()
a, b = int(InputData[0]), int(InputData[1])
if a ** b > b ** a:
    FOUT.write('GREATER')
elif a ** b < b ** a:
    FOUT.write('LESS')
else:
    FOUT.write('EQUAL')
FIN.close()
FOUT.close()
