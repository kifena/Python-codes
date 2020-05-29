n = int(input())
a = []
for j in input().split():
    a.append(int(j))
for i in range (n):
    if a[i]==1:
        print('HARD')
        break
    elif 1 not in a:
        print('EASY')
        break
