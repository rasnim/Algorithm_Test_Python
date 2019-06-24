T = int(input())

for t in range(1, T+1):
    sum = 0
    score = [int(x) for x in input().split()]

    for i in range(10):
        if score[i] % 2 == 1:
            sum += score[i]

    print("#%d %d" % (t, sum))