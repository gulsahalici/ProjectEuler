def isItAmicableNumber(number):
    sumOfDivisors = 0
    for divisor in range(1, int(number**0.5)+1):
        if number % divisor == 0:
            sumOfDivisors += divisor
            if divisor != number/divisor and divisor != 1:
                sumOfDivisors += int(number/divisor)

    return sumOfDivisors

sumOfAmicableNumbers=0

for number in range(1,10000):
    secondNum = isItAmicableNumber(number)
    if number != secondNum  and number == isItAmicableNumber(secondNum):
        sumOfAmicableNumbers += number

print(sumOfAmicableNumbers)
