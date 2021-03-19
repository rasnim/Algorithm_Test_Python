def company_a(p, w):
    result = p * w
    return result


def company_b(q, r, s, w):
    if w <= r:
        result = q
    else:
        result = q + ((w - r) * s)
    return result


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        p, q, r, s, w = map(int, input().split())

        a_result = company_a(p, w)
        b_result = company_b(q, r, s, w)

        print(f'#{t} {min(a_result, b_result)}')