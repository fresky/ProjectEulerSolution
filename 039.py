def get_traingle(number):
    result = 0
    for i in range(1, number//2):
        for j in range(max(number//2 - i,i), number//2):
            if i*i + j*j ==(number-i-j)*(number-i-j):
                result += 1
    return result

biggest = 0
answer = 0
for i in range(1, 1001):
    number = get_traingle(i)
    if number > biggest:
        biggest = number
        answer = i

print(biggest)
print(answer)
