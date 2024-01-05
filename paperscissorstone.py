import random

key_word = ['剪刀', '石頭', '布']

user = int(input('[0]剪刀, [1]石頭, [2]布:'))

rand_num = random.randint(0, 2)

print('你出了: ', key_word[user])
print('電腦出了: ', key_word[rand_num])

# ----------比較----------

# 背後是數字的比較
# 1. 是不是平手
# 2. 你是不是贏了
# 3. 電腦贏了

# if user == rand_num:
#     print('平手')
# elif (user == 0 and rand_num == 1) or (user == 1 and rand_num == 2) or (user == 2 and rand_num == 0):
#     print('電腦贏了')
# elif (user == 0 and rand_num == 2) or (user == 1 and rand_num == 0) or (user == 2 and rand_num == 1):
#     print('你贏了')

if user == rand_num:
    print('平手')
elif (user + 1) % 3 == rand_num:
    print('電腦贏了')
else:
    print('你贏了')
