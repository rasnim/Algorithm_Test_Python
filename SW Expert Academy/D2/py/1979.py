def godown(a, N, K):
    count = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                cnt = 0

                for y in range(i, N):
                    if i == 0:
                        if a[y][j] == 1:
                            cnt += 1
                        else:
                            break
                    else:
                        if a[y][j] == 1 and a[i - 1][j] == 0:
                            cnt += 1
                        else:
                            break

                if cnt == K:
                    count += 1
    return count


def goright(a, N, K):
    count = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                cnt = 0

                # 예외처리가 중요
                for x in range(j, N):
                    if j == 0:
                        if a[i][x] == 1:
                            cnt += 1
                        else:
                            break
                    else:
                        if a[i][x] == 1 and a[i][j - 1] == 0:
                            cnt += 1
                        else:
                            break

                if cnt == K:
                    count += 1
    return count


def count(a, N, K):
    count_down = godown(a, N, K)
    count_right = goright(a, N, K)

    count = count_down + count_right
    return count


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, K = map(int, input().split())

        a = []
        for i in range(N):
            a.append(list(map(int, input().split())))

        ans = 0
        ans = count(a, N, K)

        print('#' + str(t) + ' ' + str(ans))
