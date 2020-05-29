n = int(input())
c = []
if  n == 0:
    print(n)
else:
    while n > 0:
            c.append(n % 2)
            n //= 2
    c.sort(reverse=True)
    print(''.join(map(str,c)))
