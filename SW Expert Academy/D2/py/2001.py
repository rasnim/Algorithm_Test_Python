if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = input().split()
        N = int(N)
        M = int(M)

        a = [input().split() for j in range(N)]

        max_num = 0

        for i in range(0, N - M + 1):
            for j in range(0, N - M + 1):

                # Reset important
                sum_num = 0
                for k in range(i, i + M):
                    for l in range(j, j + M):
                        sum_num += int(a[k][l])
                if max_num < sum_num:
                    max_num = sum_num

        print('#' + str(t) + ' ' + str(max_num))
