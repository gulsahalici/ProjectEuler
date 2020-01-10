result=2**1000
digits=list(str(result))
sum=0
for i in range(len(digits)):
    sum+=int(digits[i])

print(sum)
