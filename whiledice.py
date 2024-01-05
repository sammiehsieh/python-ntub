import random

total = 0
count = 0

while not total > 60:
    r = random.randint(1, 6)
    total += r
    count += 1

print(total)
print(count)