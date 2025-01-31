limit = 10

prev, next = 0, 1
for i in range(limit):
    print(prev)
    prev, next = next, next + prev
