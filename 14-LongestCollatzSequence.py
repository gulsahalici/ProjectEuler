longestSequenceLength=0

for number in range(1,1000000):
  sequenceLength=1
  num=number
  
  while number!=1:  
    sequenceLength+=1
    
    if number%2==0:
      number=number/2
    else:
      number=3*number+1
      
  if sequenceLength>longestSequenceLength:
    longestSequenceLength=sequenceLength
    longestSequenceValue=num

print(longestSequenceLength)
print(longestSequenceValue)
