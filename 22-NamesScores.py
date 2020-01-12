alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
textFile=open('p022_names.txt','r')
words=sorted(textFile.read().split(","))

def getSum(name):
    sum=0
    for i in range(1,len(name)-1):
        sum+=alphabet.index(name[i])+1
    return(sum)


total=0

for name in range(len(words)):
    total+=(name+1)*getSum(words[name])

print(total)

