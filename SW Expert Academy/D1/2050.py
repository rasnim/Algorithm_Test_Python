n = input()

for i in range(len(n)):
    print(ord(n[i])-ord('A')+1, end=' ')
