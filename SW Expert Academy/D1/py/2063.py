n = int(input())

value = [int(x) for x in input().split()]

value = sorted(value)
print(value[int(n/2)])
