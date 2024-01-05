import sys

in_txt = sys.stdin.readlines()

res = []

for txt in in_txt:
    t = txt.split(" ")
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    d = int(t[3])
    resNum = 56 * a + 24 * b + 14 * c + 6 * d
    res.append(str(resNum))

print(('\n').join(res))

# multi_lines = input()

# round_num = multi_lines.splitlines()

# res = []

# for num in round_num:
#     t = num.split(" ")
#     a = int(t[0])
#     b = int(t[1])
#     c = int(t[2])
#     d = int(t[3])
#     resNum = 56 * a + 24 * b + 14 * c + 6 * d
#     res.append(str(resNum))

# print(('\n').join(res))