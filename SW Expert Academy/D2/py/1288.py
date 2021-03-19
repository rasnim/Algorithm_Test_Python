def check(check_list):
    for i in check_list:
        if i == 0:
            return 0
    return 1


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        check_list = [0 for i in range(10)]

        N = int(input())

        index = 1

        while True:
            tmp = N * index
            for s in str(tmp):
                check_list[int(s)] += 1
            if check(check_list) == 1:
                break
            index += 1

    print(f'#{t} {index * N}')
