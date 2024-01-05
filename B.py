# method 1

# user_ans = input()

# first_num = user_ans.split()[0]
# second_num = user_ans.split()[1]

# print(int(first_num) + int(second_num))


# method 2

user_ans_to_list = list(map(int, input().split()))

print(user_ans_to_list[0] + user_ans_to_list[1])
