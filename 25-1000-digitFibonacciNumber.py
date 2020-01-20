a=0
b=1
c=0
length=1
index=0
while length<1000: 
    c=a+b
    a=b
    b=c
    length=len(str(c))
    index+=1
    
print(index+1)
