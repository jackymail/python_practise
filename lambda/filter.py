import random

print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# result
# [2, 4, 6, 8, 10]


randList = list(random.randint(1, 1001) for i in range(1000))

print(list(filter((lambda x: x % 9 == 0), randList)))


