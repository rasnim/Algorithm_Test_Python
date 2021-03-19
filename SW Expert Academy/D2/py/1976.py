if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):

        a = list(map(int, input().split()))

        h_1 = a[0]
        m_1 = a[1]
        h_2 = a[2]
        m_2 = a[3]

        sum_h = h_1 + h_2
        sum_m = m_1 + m_2

        if sum_m > 60:
            sum_m = sum_m - 60
            sum_h = sum_h + 1

        if sum_h > 12:
            sum_h = sum_h - 12

        print('#%d'%t, '%d'%sum_h, '%d'%sum_m)