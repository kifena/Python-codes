n = int(input())
a = []
ans = 0
for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(n):
    if sum(a[j]) >=2:
        ans += 1
    else:
        ans = ans
print(ans)
