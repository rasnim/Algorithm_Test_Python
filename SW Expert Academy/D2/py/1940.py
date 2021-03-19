if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N = int(input())

        commands = [list(map(int, input().split())) for i in range(N)]

        v = 0
        d = 0

        for command in commands:
            if command[0] == 1:
                v += command[1]
                d += v
            elif command[0] == 2:
                if v < command[1]:
                    v = 0
                else:
                    v -= command[1]
                    d += v
            else:
                d += v

        print('#%d'%t, d)