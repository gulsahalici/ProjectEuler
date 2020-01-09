sum=0

for num in range(2,2000000):
	prime=1
	for i in range(2,1+int(num**0.5)):
		if num%i==0:
			prime=0
			break
	if prime==1:
		sum+=num

print(sum)
