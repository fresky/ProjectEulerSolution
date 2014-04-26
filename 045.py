import math

x = 144
while True:
    y = 4*x*x-2*x
    root1 = math.sqrt(4*y+1)
    if root1 == int(root1) and (root1-1)%2 == 0:
        root2 = math.sqrt(12*y+1)
        if root2 == int(root2) and (root2+1)%6==0:
            break
    x += 1

print(x*x*2-x)

