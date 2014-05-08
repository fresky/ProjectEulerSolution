import time

divisors = [2,3,5,7,11,13,17]
start = time.time()

def swap(first, second, array):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp

def get_num(start, stop, array):
    num = 0
    for i in range(start, stop):
        num = num * 10 + array[i]
    return num

def is_divisibility(array):
    for i in range(4,8):
        if get_num(i,i+3,array) % divisors[i-1] != 0:
            return False
    return True

def get_rotation(start, stop, array):
    global result
    if start == stop:
        if array[3] % 2 != 0 or array[5] % 5 != 0 or (array[2]+array[3]+array[4])% 3 != 0:
            return
        if is_divisibility(array):
            result.append(get_num(0,10,array))
        return
    for i in range(start, stop):
        swap(start, i, array)
        get_rotation(start + 1, stop, array)
        swap(start, i, array)


result = []
get_rotation(0,10,list(range(0,10)))
print(result)
print(sum(result))
print('time: ', time.time()-start)