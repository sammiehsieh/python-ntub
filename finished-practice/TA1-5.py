counties = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

user_id = input()

county_num = counties.index(user_id[0]) + 10

county_num_list = list(str(county_num))

sum_st = int(county_num_list[0]) + int(county_num_list[1]) * 9

user_num = list(user_id[1:])

sum_sec = (
    int(user_num[0]) * 8
    + int(user_num[1]) * 7
    + int(user_num[2]) * 6
    + int(user_num[3]) * 5
    + int(user_num[4]) * 4
    + int(user_num[5]) * 3
    + int(user_num[6]) * 2
    + int(user_num[7]) * 1
    + int(user_num[8]) * 1
)

total = sum_st + sum_sec

if total % 10 == 0:
    print('合法')
else:
    print('不合法')
