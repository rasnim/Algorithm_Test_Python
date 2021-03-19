if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        print('#' + str(t))
        for i in range(1, N + 1):
            if i == 1:
                print(1)
            else:
                for j in range(i):
                    if j == 0:
                        print(str(1), end=' ')
                    elif j == i - 1:
                        print(str(1))
                    else:
                        print(str(i - 1), end=' ')
