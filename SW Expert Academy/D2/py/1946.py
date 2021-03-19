if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        print('#%d'%t)
        N = int(input())
        string = ''
        for i in range(N):
            c, k = input().split()
            k = int(k)
            string = string + (c*k)

        for i in range(len(string) // 10 + 1):
            print(string[i * 10 : (i+1) * 10])