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


# fibonacci 計算

fibo_list = []  # fibonacci result

for i in range(10000):
    if i == 0:
        fibo_list.append(0)
    elif i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

del fibo_list[0]
del fibo_list[0]


# 運算結果

temp_result = []
result = []

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

def calculate_test(result, fibo_list):
    exp = ''
    cal = 0
    for i, f in enumerate(fibo_list):
        if i == 0:
            exp += str(1)
            cal += f
        else:
            cal += f
            if cal <= result:
                exp += str(1)
            else:
                exp += str(0)
                cal -= f
    return exp

for r in temp_result:
    tem = calculate_test(r['test_data'], r['fibo_list'])
    result.append(str(r['test_data']) + '=' + tem)

print('\n'.join(result))