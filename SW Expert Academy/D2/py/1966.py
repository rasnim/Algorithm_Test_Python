### 일반적인 python list의 sort 메소드 이용
if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        a = list(map(int, input().split()))
        a.sort()

        print('#%d' % t, end=' ')
        for i in range(len(a)):
            print(a[i], end=' ')
        print()
