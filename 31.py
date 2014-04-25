result = 0
target = 200
stop200 = target+1
for i200 in range(0,stop200):
    stop100 = stop200-i200*200
    for i100 in range(0,stop100):
        stop50 = stop100 - i100*100
        for i50 in range(0,stop50):
            stop20 = stop50 - i50*50
            for i20 in range(0,stop20):
                stop10 = stop20-i20*20
                for i10 in range(0, stop10):
                    stop5 = stop10-i10*10
                    for i5 in range(0, stop5):
                        stop2 = stop5 - i5*5
                        for i2 in range(0, stop2):
                            stop1 = stop2-i2*2
                            for i1 in range(0, stop1):
                                total = i1 + i2 * 2 + i5 * 5 + i10 * 10 + i20 * 20 + i50 * 50 + i100 * 100 + i200 * 200
                                if total == target:
                                    result += 1
                                elif total > target:
                                    break

print(result)



