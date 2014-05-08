import time

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


def check_pandigital(array):
    for i in range(1,5):
        base = get_num(0, i, array)
        length = len(repr(base))
        level = 2
        current = base * level
        new_len = len(repr(current))
        while length + new_len <= 9 and current == get_num(length, length + new_len, array):
            if length + new_len == 9:
                return True
            level += 1
            current = base * level
            length = length + new_len
            new_len = len(repr(current))
    return False

largest = -1
def get_rotation(start, stop, array):
    global largest
    if start == stop:
        if check_pandigital(array):
            num = get_num(0,9,array)
            if num > largest:
                largest = num
        return
    for i in range(start, stop):
        if largest > 0:
            return largest
        swap(start, i, array)
        get_rotation(start + 1, stop, array)
        swap(start, i, array)


get_rotation(0,9,[9,8,7,6,5,4,3,2,1])
print(largest)
print('time: ', time.time()-start)

