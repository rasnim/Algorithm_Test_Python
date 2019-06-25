T = int(input())

for t in range(1, T+1):
    sum = 0
    average = 0
    score = [int(x) for x in input().split()]

    for i in range(10):
        sum += score[i]
        average = sum / len(score)

    print("#%d %d" % (t, round(average)))