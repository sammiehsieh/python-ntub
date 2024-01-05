# user_num = int(input())


# non_prime_nums = []

# i = user_num
# while i > 1:
#     k = user_num - 1
#     while k > 1:
#         if i != k:
#             if (i % k) == 0:
#                 if i not in non_prime_nums:
#                     non_prime_nums.append(i)
#         k -= 1
#     i -= 1

# # print(non_prime_nums)


# result = user_num

# n = 0
# while n <= user_num:
#     if n not in non_prime_nums:
#         result = n
#     n += 1

# print(result)



# Bard'a answer

n = int(input())

# 從 2 開始，依序檢查是否為質數
max_prime = 2
for i in range(3, n + 1):
    # 檢查是否為質數
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        # 是質數
        max_prime = i

# 輸出最大質數
print("小於等於 {} 的最大質數是 {}".format(n, max_prime))

