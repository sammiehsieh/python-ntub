lotte = input()

my_num_list = lotte.split(',')[0].split(' ')

award_num_list = lotte.split(',')[1].split(' ')

match_num = 0

if my_num_list[0] in award_num_list:
    match_num = match_num+1
if my_num_list[1] in award_num_list:
    match_num += 1
if my_num_list[2] in award_num_list:
    match_num += 1
if my_num_list[3] in award_num_list:
    match_num += 1
if my_num_list[4] in award_num_list:
    match_num += 1

if match_num == 3:
    print(100)
elif match_num == 4:
    print(1000)
elif match_num == 5:
    print(10000)
else:
    print(0)