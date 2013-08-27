

previous = 2
current = 8
limit = 4000000
total = 2

for i in range(limit):
    total += current
    next = previous+4*current
    if next > limit:
        break
    previous = current
    current = next

print(total)

