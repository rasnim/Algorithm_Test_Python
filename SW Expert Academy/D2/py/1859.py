if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N = int(input())

        a = []
        b = list(map(int, input().split()))

        for i in range(0, N):
            a.append(int(b[i]))

        ans = 0
        max_num = 0

        for j in reversed(range(0, N)):
            if max_num > a[j]:
                ans += max_num-a[j]
            else:
                max_num = a[j]

        print(f'# {t} {ans}')

        ans = 0
        max_num = 0