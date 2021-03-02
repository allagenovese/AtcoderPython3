n = int(input())
d = [int(input()) for _ in range(n)]
num = set()
for i in d :
    num.add(i)
print(len(num))
