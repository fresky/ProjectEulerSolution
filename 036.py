

def is_palindromes(num):
    str = list(num)
    str.reverse()
    return num == ''.join(str)

def get2base(i):
    result = ''
    while i >1:
        result += repr(i%2)
        i = i//2
    result += repr(i)
    return result

answer = []
for i in range(1,1000000):
    if is_palindromes(repr(i)):
        if is_palindromes(get2base(i)):
            answer.append(i)

print(sum(answer))
