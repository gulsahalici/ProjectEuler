x=600851475143
cnt=1

while x!=1:
	if x%cnt==0:
		x=x/cnt
	cnt=cnt+1

print(cnt)
