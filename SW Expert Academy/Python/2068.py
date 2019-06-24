T = int(input())

for t in range(1, T+1):
    max = 0;
    score = [int(x) for x in input().split()]

    for i in range(10):
        b = score[i]
        if b > max:
            max = b

    print("#%d %d" % (t, max))