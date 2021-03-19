def counting(N):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while N % 2 == 0:
        N = N // 2
        a += 1

    while N % 3 == 0:
        N = N // 3
        b += 1

    while N % 5 == 0:
        N = N // 5
        c += 1

    while N % 7 == 0:
        N = N // 7
        d += 1

    while N % 11 == 0:
        N = N // 11
        e += 1

    return a, b, c, d, e


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        a, b, c, d, e = counting(N)
        print('#%d' % t, a, b, c, d, e)
