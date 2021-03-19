def distance_cal(t, count, base_dist, dist_list):
    for i in range(1, len(dist_list)):
        if abs(0 - dist_list[i]) < base_dist:
            base_dist = abs(0 - dist_list[i])
        elif abs(0 - dist_list[i]) == base_dist:
            base_dist = base_dist
            count += 1
        else:
            base_dist = base_dist

    print(f'#{t} {base_dist} {count}')


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        dist_list = list(map(int, input().split()))

        count = 1
        base_dist = abs(dist_list[0])

        distance_cal(t, count, base_dist, dist_list)
