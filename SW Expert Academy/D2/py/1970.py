def change_money(a, N, index, money):
    if N >= money:
        N = N - money
        a[index] += 1
        a, N = change_money(a, N, index, money)
    return a, N


def change(a, N):
    a_50000, N_50000 = change_money(a, N, 0, 50000)
    a_10000, N_10000 = change_money(a_50000, N_50000, 1, 10000)
    a_5000, N_5000 = change_money(a_10000, N_10000, 2, 10000)
    a_1000, N_1000 = change_money(a_5000, N_5000, 3, 5000)
    a_500, N_500 = change_money(a_1000, N_1000, 4, 1000)
    a_100, N_100 = change_money(a_500, N_500, 5, 500)
    a_50, N_50 = change_money(a_100, N_100, 6, 100)
    a_10, N_10 = change_money(a_50, N_50, 7, 50)
    return a_10


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())

        a = [0] * 8
        a = change(a, N)

        print('#%d' % t)

        for i in range(8):
            print(a[i], end=' ')
        print()
