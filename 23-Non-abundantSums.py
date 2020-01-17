from math import sqrt

def getAbundant(number):
    sumDivisors=1
    for divisor in range(2,int(sqrt(number))+1):
        if number%divisor==0:
            sumDivisors+=divisor
            if number/divisor!=divisor:
                sumDivisors+=number/divisor
                
    if number<sumDivisors:
        return 1
    else:
        return 0

NonAbundantSums=0
isAbundant=0
for num in range(1,28123):
    for firstNum in range(1,num):
        secondNum=num-firstNum
        if getAbundant(firstNum)==1 and getAbundant(secondNum)==1:
            isAbundant=1
            break

    if isAbundant==0:
        NonAbundantSums+=num
        
    isAbundant=0
    
print(NonAbundantSums)
