total = int(input())

round_num = 0

while total != 0:
    round_num += 1
    if (total % 2) == 1:
        total -= 1
    else:
        total = total // 2

print(round_num)