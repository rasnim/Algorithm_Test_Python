class arrayrotate:
    def __init__(self):
        return

    def rotate(a, N):
        arr = [[0 for i in range(N)] for j in range(N)]

        for j in range(N):
            arr[j][N - 1] = a[0][j]
            arr[j][0] = a[N - 1][j]

        for i in range(N):
            for j in range(N):
                arr[j][N - 1 - i] = a[i][j]

        return arr, N


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        a = []
        for i in range(N):
            a.append(list(map(int, input().split())))

        rotate_90, N = arrayrotate.rotate(a, N)
        rotate_180, N = arrayrotate.rotate(rotate_90, N)
        rotate_270, N = arrayrotate.rotate(rotate_180, N)

        print('#%d' % t)
        for i in range(N):
            for j in range(N):
                print(rotate_90[i][j], end='')
            print(end=' ')
            for j in range(N):
                print(rotate_180[i][j], end='')
            print(end=' ')
            for j in range(N):
                print(rotate_270[i][j], end='')
            print(end=' ')
            print()
