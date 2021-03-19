def solve(score):
    max_num_count = 0
    max_num_value = 0

    for i in range(100, -1, -1):
        count = score.count(i)

        if max_num_count < count:
            max_num_count = count
            max_num_value = i

    return max_num_value


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        tnum = int(input())
        score = list(map(int, input().split()))

        print(f'#{tnum} {solve(score)}')
