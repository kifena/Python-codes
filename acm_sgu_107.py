n = int(input())
c = []
while n > 0:
	c.append (n % 2)
	n //= 2
c.sort(reverse=True)
print(''.join(map(str,c)))
