__author__ = 'Dawei'

words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'
    ,11:'eleven',12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen'
    , 16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen', 20:'twenty'}
twowords = {2:'twenty'
    , 3:'thirty', 4:'forty', 5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
threewords = {100:'hundred'}
fourwords = {1000:'thousand'}

def getonewordcount(n):
    if n == 0:
        return 0
    return len(words[n])

def gettwowordcount(n):
    return getonewordcount(n%10)+ len(twowords[n//10])

def getthreewordcount(n):
    result = getonewordcount(n//100) + len('hundred')
    if n%100 != 0:
        result += len('and')
    if n%100 <=20:
        return result + getonewordcount(n%100)
    else:
        return result + gettwowordcount(n%100)

def getwordcount(n):
    if n<=20:
        return getonewordcount(n)
    elif n < 100:
        return gettwowordcount(n)
    else:
        return getthreewordcount(n)


result = 0
for i in range(1, 1000):
    result += getwordcount(i)

result += len('onethousand')

print(result)

result = 0
for i in range(1,6):
    result += getwordcount(i)

print(result)