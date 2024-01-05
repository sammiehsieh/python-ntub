num_arr = [0]

human_index = int(input())

i = 1

while i < human_index:
    if i == 1:
        num_arr.append(1)
    else:
        result = num_arr[i - 1] + num_arr[i - 2]
        num_arr.append(result)
    i += 1

print(num_arr[human_index - 1])