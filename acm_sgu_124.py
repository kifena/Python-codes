n = int(input())
a = []
for i in input().split():
    a.append(int(i))
ans = []
c = list(set(a))
c.sort(reverse = True)
ans.append(c[0])
ans.append(c[1])
ans.append(c[2])
print(ans)
