def get_gcd(a,b):
    while a%b != 0:
        a = a%b
        a,b = b,a
    return b


def get_lcm(a,b):
    return a*b//get_gcd(a,b)

result = 1
for i in range(2,21):
    result = get_lcm(result, i)

print(result)


