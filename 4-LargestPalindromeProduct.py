max=0

for first in range(1000,100,-1):
	for second in range(1000,100,-1):
		multp=first*second
		listt=list(str(multp))
		reverse=""
		for x in  range(len(listt)-1,-1,-1):
			reverse=reverse+listt[x]
		if multp==int(reverse):
			if multp>max:
				max=multp

print(max)
