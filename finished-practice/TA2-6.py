## answer from google search

def fib(n):
    f = [0, 1]
    if n <= 1:
        return n
    for i in range(2, n + 1):
        f[0], f[1] = f[1], f[0] + f[1]
    return f[1]

while True:
    try:
        a, b, c, d = map(int, input().split())
        r = 56 * a + 24 * b + 14 * c + 6 * d
        print(fib(r))
    except:
        break