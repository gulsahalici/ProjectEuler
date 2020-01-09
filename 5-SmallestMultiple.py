sum=0
num=3000

while sum!=20:
	sum=0
	num=num+10
	for i in range(1,21):
		if num%i==0:
			sum=sum+1

print(num)
