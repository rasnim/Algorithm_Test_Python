def month_day(m):
    if m == 1:
        day = 31
    elif m == 2:
        day = 28
    elif m == 3:
        day = 31
    elif m == 4:
        day = 30
    elif m == 5:
        day = 31
    elif m == 6:
        day = 30
    elif m == 7:
        day = 31
    elif m == 8:
        day = 31
    elif m == 9:
        day = 30
    elif m == 10:
        day = 31
    elif m == 11:
        day = 30
    else:
        day = 31

    return day


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        day = 0
        sum_m2day = 0
        sum_m1day = 0

        a = list(map(int, input().split()))

        m_1 = a[0]
        d_1 = a[1]
        m_2 = a[2]
        d_2 = a[3]

        for i in range(1, m_2):
            sum_m2day += month_day(i)
        sum_m2day += d_2

        for j in range(1, m_1):
            sum_m1day += month_day(j)
        sum_m1day += d_1

        day = sum_m2day - sum_m1day + 1

        print('#%d' % t, day)
