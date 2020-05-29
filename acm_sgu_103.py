FIN  = open('input.txt',  'r')
FOUT = open('output.txt', 'w')
InputData = FIN.read()
d = [str(x) for x in InputData]
c = []
c.append('P'*(d.count('P')))
c.append('K'*(d.count('K')))
c.append('S'*(d.count('S')))
c.append('L'*(d.count('L')))
c.append('F'*(d.count('F')))
FOUT.write(''.join(c))
FIN.close()
FOUT.close()
