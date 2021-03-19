if __name__ == '__main__':
    N = int(input())

    for i in range(1, N+1):
        if list(str(i)).count('3') == 0 and list(str(i)).count('6') == 0 and list(str(i)).count('9') == 0:
            print(i, end=' ')
            # 3이 아닌 경우
        else:
            # 3인 경우
            arr = list(str(i))
            for i in range(len(arr)):
                x = arr.pop()
                if x == '3' or x == '6' or x == '9':
                    print('-', end='')
            print('', end=' ')