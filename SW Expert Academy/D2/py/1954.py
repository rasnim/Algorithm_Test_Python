if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        start = 1
        arr = [[0] * N for i in range(N)]

        for i in range(N // 2):
            for j in range(i, N - i):
                arr[i][j] = start
                start += 1

            for j in range(i + 1, N - i):
                arr[j][N - 1 - i] = start
                start += 1

            for j in range(N - 1 - i, i, -1):
                arr[N - 1 - i][j - 1] = start
                start += 1

            for j in range(N - 2 - i, i, -1):
                arr[j][i] = start
                start += 1

        if N % 2 == 1:
            arr[(N - 1) // 2][(N - 1) // 2] = start

        print('#%d' % t)
        for i in range(N):
            for j in range(N):
                print(arr[i][j], end=' ')
            print()
