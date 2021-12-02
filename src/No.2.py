
n=input().split()
n=set(n)
for i in sorted(n):
	print(i, end=' ')

#----------------------------------------------------

print(*(sorted(set(map(int, input().split())))))
