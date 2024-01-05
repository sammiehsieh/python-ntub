# U up
# D down
# L left
# R right

x = 0
y = 0

move = list(input())

for i in move:
    if i == 'U':
        y += 1
    if i == 'D':
        y -= 1
    if i == 'R':
        x += 1
    if i == 'L':
        x -= 1

if x == 0 and y == 0:
    print('Y')
else:
    print('N')