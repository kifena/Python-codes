a = int(input())
b = int(input())
c = int(input())
k = []
k.append(max(a, b, c))
k.append(min(a, b, c))
if a not in k:
    print (a)
elif c not in k:
    print (c)
else:
    print (b)
