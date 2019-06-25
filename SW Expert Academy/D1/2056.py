T = int(input())

for t in range(1, T+1):
    n = input()
    y = n[0] + n[1] + n[2] + n[3]
    m = n[4] + n[5]
    d = n[6] + n[7]

    sm = int(m)
    sd = int(d)

    if sm > 12 or sm < 1:
        print('#%d -1'%(t))
    else:
        if sm == 2:
            if sd > 0 and sd < 29:
                print('#%d %s/%s/%s' % (t, y, m, d))
            else:
                print('#%d %d' % (t, -1))

        elif sm <= 7:
            if sm % 2 == 1:
                if sd > 0 and sd < 32:
                    print('#%d %s/%s/%s' % (t, y, m, d))
                else:
                    print('#%d %d' % (t, -1))
            else:
                if sd > 0 and sd < 31:
                    print('#%d %s/%s/%s' % (t, y, m, d))
                else:
                    print('#%d %d' % (t, -1))

        elif sm >= 8:
            if sm % 2 == 1:
                if sd > 0 and sd < 31:
                    print('#%d %s/%s/%s' % (t, y, m, d))
                else:
                    print('#%d %d' % (t, -1))
            else:
                if sd > 0 and sd < 32:
                    print('#%d %s/%s/%s' % (t, y, m, d))
                else:
                    print('#%d %d' % (t, -1))