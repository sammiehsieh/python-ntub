# method 1

# user_input = input()

# i = user_input.split(' ')

# week = i[0]

# stock_price = int(i[1])

# volume = int(i[2])

# if week == '星期五' or week == '星期六' or week == '星期日':
#     print('不開市')
# else:
#     print(stock_price * volume)



# method 2

all_week = ['星期五', '星期六', '星期日']

user_input = input()

i = user_input.split(' ')

week = i[0]

stock_price = int(i[1])

volume = int(i[2])

if week in all_week:
    print('不開市')
else:
    print(stock_price * volume)
