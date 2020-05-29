n = int(input())
m = int(input())
a = []
for x in range (n):
    a.append(int(input()))
maximum = max(a) + m
for i in range(n):
    if a[i] >= m:
        break
    else:
        a[i]+=1
        m -= 1
mimimum = max(a)
print(maximum, mimimum)
