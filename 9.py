sum = 1000
for i in range(1,sum//2):
    if  (sum*sum/2-sum*i)% (sum-i)==0:
        a = i
        b = int(((sum*sum)/2-sum*i)//(sum-i))
        break

print(a*b*(sum-a-b))