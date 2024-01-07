import sys

in_txt = sys.stdin.readlines()

# 解析題目成資料

input_for_range = 0  # 幾組資料要測試
input_test_data = []  # 測試資料

for i, txt in enumerate(in_txt):
    t = txt.split("\n")[0]
    if i == 0:
        input_for_range = int(t)
    else:
        input_test_data.append(int(t))

print('for range', input_for_range)
print('test data', input_test_data)

# fibonacci 計算

fibo_list = []  # fibonacci result

for i in range(17):
    if i == 0:
        fibo_list.append(0)
    elif i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

del fibo_list[0]
del fibo_list[0]

print('fibo list', fibo_list)

# 運算結果

temp_result = []

for d in input_test_data:
    # 在 fibo_list 中一個一個找，小於等於 d 的為一定要加入(即為1)，再從陣列裡湊
    fibo_using = []
    i = 0
    while fibo_list[i] <= d:
        fibo_using.append(fibo_list[i])
        i += 1
    sort_reversed = sorted(fibo_using, reverse=True)
    temp_result.append({
        'test_data': d,
        'fibo_list': sort_reversed
    })

# print(temp_result)


def calculate_test(result, fibo_list):
    exp = ''
    for i, f in enumerate(fibo_list):
        cal = 0
        if i == 0:
            exp += str(1)
            cal += f
        # elif cal == result:
        #     exp += str(0)
        # else:
        #     cal += f
        #     if cal > result:
        #         exp += str(0) # 加起來大於，不要了
        #         cal -= f
        #     elif cal == result:
        #         exp += str(1) # 加起來相等，結束
        #     else:
        #         exp += str(1) # 加起來小於，繼續
        # print('i', i, 'cal', cal)
    return exp


for r in temp_result:
    result = calculate_test(r['test_data'], r['fibo_list'])
    print(str(r['test_data']) + '=' + result)
