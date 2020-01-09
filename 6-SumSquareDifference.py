sumOfSquares=0
squareOfSum=0

for i in range(101):
	sumOfSquares+=i**2
	squareOfSum+=i

print(squareOfSum**2-sumOfSquares)
