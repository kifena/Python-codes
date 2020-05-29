FOUT = open('output.txt','w')
begining = open('input.txt','r')
p = begining.read()
o = p//100
g = p%100
if g > 0:
    if g >=10:
        j = g//10
        if (g %10) > 0:
            x = (g%10)
        else:
            x = 0
    else:
        j = g
        x = 0
else:
    j = 0
    x = 0
FOUT.write(o+x+j)
FOUT.close()
begining.close()
