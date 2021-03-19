def count(a, n):
    flag = 0

    answer_row = checkR(a, n, flag)
    answer_col = checkC(a, n, flag)
    answer_squ = checkRC(a, n, flag)

    if answer_row == 0 and answer_col == 0 and answer_squ == 0:
        answer = 1
    else:
        answer = 0
    return answer


def checkR(a, n, flag):
    answer_row = flag
    for i in range(n):
        # 배열 초기화 값 설정
        arr = [0] * (n + 1)
        for j in range(n):
            if arr[a[i][j]] != 0:
                answer_row = 1
                break
            else:
                arr[a[i][j]] = 1
    return answer_row


def checkC(a, n, flag):
    answer_col = flag
    for j in range(n):
        # 배열 초기화 값 설정
        arr = [0] * (n + 1)
        for i in range(n):
            if arr[a[i][j]] != 0:
                answer_col = 1
                break
            else:
                arr[a[i][j]] = 1
    return answer_col


def checkRC(a, n, flag):
    answer_squ = flag
    for i in range(0, n, 3):
        # 배열 초기화 값 설정
        arr = [0] * (n + 1)
        for j in range(0, n, 3):
            arr[a[i][j]] = 1
            arr[a[i][j + 1]] = 1
            arr[a[i][j + 2]] = 1

            arr[a[i + 1][j]] = 1
            arr[a[i + 1][j + 1]] = 1
            arr[a[i + 1][j + 2]] = 1

            arr[a[i + 2][j]] = 1
            arr[a[i + 2][j + 1]] = 1
            arr[a[i + 2][j + 2]] = 1

            for k in range(1, 10):
                if arr[k] != 1:
                    answer_squ = 1
                    break
    return answer_squ


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        a = []
        n = 9
        for i in range(n):
            a.append(list(map(int, input().split())))

        answer = count(a, n)

        print('#%d' % t, '%d' % answer)
