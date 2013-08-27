def is_palindromic(number):
    list=[]
    while number//10 >0:
        list.append(number%10)
        number = number//10
    list.append(number)
    newlist = list[:]
    newlist.reverse()
    return newlist == list



def is_product(product):
    for i in range(999, 0,-1):
        if product%i==0 and product//i >99 and product//i<1000:
            return True
    return False

def find_largest(product):
    for i in range(product, 0, -1):
        if is_product(i) and is_palindromic(i):
            return i
    return 0

print(find_largest(999*999))



