FIN = open('input.txt','r')
FOUT = open('output.txt','w')
InputData = FIN.read().split()
a,b,c = InputData[0],InputData[1],InputData[2]
FOUT.write(str(len(set([a,b,c]))))
FIN.close()
FOUT.close()
