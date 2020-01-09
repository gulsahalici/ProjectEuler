
def pythagorean():
	for a in range(1000):
		for b in range(1000):
			for c in range(1000):
				if a<b and b<c:
					if a**2+b**2==c**2 and a+b+c==1000:
						return a*b*c

print(pythagorean())
