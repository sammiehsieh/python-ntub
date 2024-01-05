import sys

in_txt = sys.stdin.readlines()

input_for_range = 0
input_test_data = []

for i, txt in enumerate(in_txt):
    t = txt.split("\n")[0]
    if i == 0:
        input_for_range = int(t)
    else:
        input_test_data.append(int(t))

print('for range', input_for_range)
print('test data', input_test_data)


fibo_list = []

for i in range(17):
    if i == 0:
        fibo_list.append(0)
    elif i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

print('fibo list', fibo_list)


for d in input_test_data:
    print(d)