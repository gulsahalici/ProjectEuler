listt=[]
index=0
num=1

while index!=10001:
	prime=0
	num+=1
	for j in range(1,num):
		if num%j==0:
			prime+=1
		if prime>1:
			break
	if prime==1:
		index+=1
		listt.append(num)

print(listt[10000])
