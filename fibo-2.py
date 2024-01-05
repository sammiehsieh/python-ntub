from functools import lru_cache


@lru_cache(maxsize=999999)
def fibo(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    return fibo(n - 1) + fibo(n - 2) + fibo(n - 3)


print(fibo(6))
