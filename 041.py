import time
import math

start = time.time()

def swap(first, second, array):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp

def get_num(array):
    num = 0
    for i in array:
        num = num * 10 + i
    return num

def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

largest = -1
def get_rotation(start, stop, array):
    global largest
    if start == stop:
        num = get_num(array)
        if is_prime(num) and num > largest:
            largest = num
        return
    for i in range(start, stop):
        if largest > 0:
            return largest
        swap(start, i, array)
        get_rotation(start + 1, stop, array)
        swap(start, i, array)

def get_largest():
    for i in range(9,0,-1):
        array = list(range(i, 0, -1))
        if sum(array) == 3:
            continue
        get_rotation(0,len(array), array)
        if largest > 0:
            return largest

print(get_largest())
print('time: ', time.time()-start)
