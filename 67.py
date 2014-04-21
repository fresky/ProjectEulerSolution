
file_object = open('67.txt', 'r')
triangle = file_object.readlines()

row = len(triangle)

array = []
for line in triangle:
    array += [int(s) for s in line.split()]

for i in range(row,1,-1):
    lastrow = array[-i:]
    array = array[0:-i]
    for j in range(len(lastrow)-1):
        if lastrow[j] < lastrow[j+1]:
            array[j+1-len(lastrow)] += lastrow[j+1]
        else:
            array[j+1-len(lastrow)] += lastrow[j]
print(array[0])
