numbers=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

numFirst=""
numSecond=""

for number in range(20,100):
    section=number/10
    remaining=number%10

    if section==2:
        numFirst="twenty"
    if section==3:
        numFirst="thirty"
    if section==4:
        numFirst="forty"
    if section==5:
        numFirst="fifty"
    if section==6:
        numFirst="sixty"
    if section==7:
        numFirst="seventy"
    if section==8:
        numFirst="eighty"
    if section==9:
        numFirst="ninety"

    if remaining!=0:
        numSecond=numbers[remaining-1]
    else:
        numSecond=""
        
    numberr=numFirst+numSecond
    numbers.append(numberr)

for num in range(100,1000):
    section=int(num/100)
    remaining=num%100

    if remaining==0:
        numFirst=numbers[section-1]+"hundred"
        numSecond=""
    else:
        numFirst=numbers[section-1]+"hundredand"
        numSecond=numbers[remaining-1]

    numbr=numFirst+numSecond
    numbers.append(numbr)

numbers.append("onethousand")
lettersNumber=0


for i in range(1000):
    lettersNumber+=len(numbers[i])

print(lettersNumber)

    
    
