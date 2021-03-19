if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        ans = 0
        a = input().split()
        a = [int(i) for i in a]

        sum_num = 0

        for i in range(len(a)):
            sum_num += a[i]

        min_num = a[0]
        max_num = a[0]
        for j in range(0, len(a)):

            if a[j] < min_num:
                min_num = a[j]
            elif a[j] > max_num:
                max_num = a[j]

        sum_num -= min_num
        sum_num -= max_num
        ans = round(sum_num / 8)

        print('#' + str(t) + ' ' + str(ans))
