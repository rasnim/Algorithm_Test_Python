T = int(input())

for t in range(1, T+1):
    score = [int(x) for x in input().split()]

    a = score[0]
    b = score[1]

    print("#%d %d %d" % (t, (a/b), (a%b)))