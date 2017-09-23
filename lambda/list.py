import random

flipList = []

for i in range(1,1000):
    flipList += random.choice(['H','T'])

print("Heads :",flipList.count('H'))
print("Tails :",flipList.count('T'))




