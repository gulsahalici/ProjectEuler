def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)

digits=list(str(factorial(100)))

sum=0
for i in range(len(digits)):
    sum+=int(digits[i])

print(sum)
