if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N, K = input().split()
        N = int(N)
        K = int(K)

        score = 0

        a = []
        for i in range(0, N):
            mid, fin, hom = input().split()
            a.append(int(mid) * 0.35 + int(fin) * 0.45 + int(hom) * 0.2)

        score = a[K-1]
        a.sort()
        b = a.index(score)
        per = int((b/N) * 10)

        if per == 0:
            answer = 'D0'
        elif per == 1:
            answer = 'C-'
        elif per == 2:
            answer = 'C0'
        elif per == 3:
            answer = 'C+'
        elif per == 4:
            answer = 'B-'
        elif per == 5:
            answer = 'B0'
        elif per == 6:
            answer = 'B+'
        elif per == 7:
            answer = 'A-'
        elif per == 8:
            answer = 'A0'
        else:
            answer = 'A+'

        print('#'+str(t)+' '+answer)