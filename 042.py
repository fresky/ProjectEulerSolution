import math

file_object = open('042.txt', 'r')
words = file_object.readline().replace('"','').split(',')

def is_traingle(value):
    if value == 0:
        return False
    a = int(math.sqrt(2*value))
    return 2*value == a*(a+1)

result = 0


def get_value(word):
    value = 0
    for c in word:
        value += ord(c) - ord('A')+1
    return value

for word in words:
    value = get_value(word)
    if is_traingle(value):
        result += 1

print(result)

