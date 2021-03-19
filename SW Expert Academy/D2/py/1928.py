import base64


def base64_string(a):
    string = base64.b64decode(a).decode('utf-8')
    return string


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        a = input()
        string = base64_string(a)

        print('#{} {}'.format(t, string))
