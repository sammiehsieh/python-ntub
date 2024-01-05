user_input = input()

user_input_list = user_input.split(" ")

i = int(user_input_list[0]) - 1

del user_input_list[0]

names = user_input_list

print(names[i])
