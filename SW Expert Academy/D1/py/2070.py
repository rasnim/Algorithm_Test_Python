T = int(input())

for t in range(1, T + 1):
    score = [int(x) for x in input().split()]

    a = score[0]
    b = score[1]

    if a > b:
        value = ">"
        print("#%d %s" % (t, value))
    elif a == b:
        value = "="
        print("#%d %s" % (t, value))
    else:
        value = "<"
        print("#%d %s" % (t, value))
