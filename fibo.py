# recursion

# fibonacci array

# 0 1 1 2 3 5 8 13 21 34 55...

# def fibo(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(10)) # 55


# 加上 cache
# recursion + cache = dynamic programming

# cache = {}
# def fibo(n: int) -> int:
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     cache[n] = fibo(n-1) + fibo(n-2)
#     return cache[n]

# print(fibo(100))


# python 內建快取機制
# @裝飾器 decorator

from functools import lru_cache

@lru_cache(maxsize=999999)
def fibo(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(100))