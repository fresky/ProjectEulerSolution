import time

def get_all():
        result = []
        number1 = set(range(1,10))
        for i1 in number1:
            number2 = set(number1)
            number2.remove(i1)
            for i2 in number2:
                number3 = set(number2)
                number3.remove(i2)
                for i3 in number3:
                    number4 = set(number3)
                    number4.remove(i3)
                    for i4 in number4:
                        number5 = set(number4)
                        number5.remove(i4)
                        for i5 in number5:
                            number6 = set(number5)
                            number6.remove(i5)
                            for i6 in number6:
                                number7 = set(number6)
                                number7.remove(i6)
                                for i7 in number7:
                                    number8 = set(number7)
                                    number8.remove(i7)
                                    for i8 in number8:
                                        number9 = set(number8)
                                        number9.remove(i8)
                                        for i9 in number9:
                                            result.append(
                                                repr(i1) + repr(i2) + repr(i3) + repr(i4) + repr(i5) + repr(i6) + repr(
                                                    i7) + repr(i8) + repr(i9))
        return result

def str_num():
    all = get_all()
    answer = set()
    for str in all:
        if int(str[0]) * int(str[1:-4]) == int(str[-4:]):
            answer.add(int(str[-4:]))
        elif int(str[0:2]) * int(str[2:-4]) == int(str[-4:]):
            answer.add(int(str[-4:]))
    print(sum(answer))

def num_str():
    answer = set()
    for i in range(1,10):
        for j in range(1000,9999):
            product = i * j
            if product > 9999:
                break
            digits = set([s for s in repr(i) + repr(j) + repr(product)])
            if '0' not in digits and len(digits) == 9:
                answer.add(product)
    for i in range(10,100):
        for j in range(100,999):
            product = i * j
            if product > 9999:
                break
            digits = set([s for s in repr(i) + repr(j) + repr(product)])
            if '0' not in digits and len(digits) == 9:
                answer.add(product)
    print(sum(answer))

start = time.time()
str_num()
print(time.time() - start)

start = time.time()
num_str()
print(time.time() - start)









