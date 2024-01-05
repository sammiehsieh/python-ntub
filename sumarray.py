data = [1, 2, 3, 5, 6, 7, 9, 10]
target = 12
ans = []
i = 0

while i < len(data):
    k = 0
    # k = i # Q1(answer)
    # k = i + 1 # Q2(answer)
    while k < len(data):
        if data[i] + data[k] == target:
            ans.append([data[i], data[k]])
        k += 1
    i += 1

print(ans)

# Q1. [3,9] 和 [9,3] 當作一樣
# Q2. [6,6] 不能算
