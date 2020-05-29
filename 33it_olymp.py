m = int(input())
k = 1
d = 2
while d * d <=m:
    if m % (d * d) == 0:
        k = d * d
    d +=1
print (k)
