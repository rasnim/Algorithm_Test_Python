def multiple(a, b, N, M):
    max_num = 0
    if N < M:
        for i in range(M - N + 1):
            c = 0
            sum_c = 0
            for j in range(N):
                c = a[j] * b[i + j]
                sum_c += c
            if max_num < sum_c:
                max_num = sum_c

    elif N == M:
        for i in range(N):
            c = a[i] * b[i]
            max_num += c

    else:
        for i in range(N - M + 1):
            c = 0
            sum_c = 0
            for j in range(M):
                c = a[i + j] * b[j]
                sum_c += c
            if max_num < sum_c:
                max_num = sum_c
    return max_num


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = map(int, input().split())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        max_num = multiple(a, b, N, M)

        print('#%d' % t, max_num)
