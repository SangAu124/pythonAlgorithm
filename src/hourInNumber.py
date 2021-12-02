
h=int(input())
count=0
for i in range(h+1):
	for j in range(60):
		for k in range(60):
			ss=str(i)+str(j)+str(k)
			if '3' in ss:
				count += ss.count('3')
print(count)

