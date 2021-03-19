if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        a = input()
        N = len(a)
        count = 1

        for i in range(1, N):
            if a[0] == a[i] and a[1] == a[i + 1]:
                break
            else:
                count += 1
        print('#' + str(t) + " " + str(count))
