if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        ans = 0

        N = int(input())

        sum_num = 0
        for i in range(1, N + 1):
            if i % 2 == 0:
                sum_num -= i
            else:
                sum_num += i
        ans = sum_num

        print('#' + str(t) + ' ' + str(ans))
