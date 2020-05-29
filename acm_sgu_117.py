n = int(input())
c = 0
for i in range (n):
    if i % 2 == 1:
        c += 1
    else:
        c = c
print(c)
