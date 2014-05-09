def is_valid(num, ori_set):
    cur_set = set()
    while num > 0:
        if num%10 not in ori_set:
            return False
        cur_set.add(num%10)
        num = num//10
    return cur_set == ori_set

def get_permuted():
    digit = 1
    while True:
        begin = 10**(digit-1)
        limit = 10**digit//6 + 1
        for i in range(begin, limit):
            if i == 0:
                continue
            set1 = set()
            num = i
            while num > 0:
                set1.add(num%10)
                num = num//10
            found = True
            for j in range(2,7):
                if not is_valid(j*i, set1):
                    found = False
                    break
            if found:
                return i
        digit +=1

print(get_permuted())



