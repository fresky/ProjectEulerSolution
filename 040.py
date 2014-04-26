import math
def getLength(n):
    return int(math.pow(10,n)-math.pow(10,n-1))*n

def getNumber(n):
    i = 1
    preLength = 0
    while True:
        length = getLength(i)+preLength
        if length>=n:
            if i == 1:
                return n
            if (n-preLength)%i==0:
                index = (n-preLength)//i
                position = i
            else:
                index = (n-preLength)//i + 1
                position = (n-preLength)%i
            number = int(math.pow(10,i-1)) + index-1

            return (number%int(math.pow(10,i-position+1)))//int(math.pow(10,i-position))
        i+=1
        preLength = length

result = 1
for i in range(7):
    number = getNumber(int(math.pow(10, i)))
    result *= number

print(result)