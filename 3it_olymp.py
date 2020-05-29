m = int(input())
k = []
for i in range (1, m+1):
    if m % (i**2) == 0:
        k.append (i**2)
print (max(k))
