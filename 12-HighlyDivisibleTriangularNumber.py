i=0
number=0
divisor=0

while divisor<=500:
    divisor=0
    i+=1
    number+=i
    for j in range(1,int(number**0.5)+1):
        if number%j==0:
            divisor+=1
    divisor=2*divisor
    
print(divisor)
print(number)

