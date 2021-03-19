score = [int(x) for x in input().split()]
p = score[0]
k = score[1]
count = 0

for count in range(p+1-k):
    count = count + 1
print(count)