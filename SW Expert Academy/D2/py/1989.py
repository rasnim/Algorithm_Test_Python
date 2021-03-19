if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        ans = 0

        a = []
        b = []

        words_a = list(input())
        words_b = words_a[:]

        while words_a:
            a.append(words_a.pop())
            b.append(words_b.pop(0))

        if a == b:
            ans += 1

        print('#' + str(t) + ' ' + str(ans))
        ans = 0
