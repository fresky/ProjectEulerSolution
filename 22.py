file_object = open('22.txt', 'r')
line = file_object.readline()
names = line.replace('"', '').split(',')
names.sort()

result = 0
for j in range(len(names)):
    sum = 0
    for c in names[j]:
        sum += ord(c)-ord('A')+1
    result += sum * (j+1)

print(result)