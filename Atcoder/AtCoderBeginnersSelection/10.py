n = int(input())
xyt = [map(int, input().split()) for _ in range(n)]
t, x, y = [list(i) for i in zip(*xyt)]
x1 = 0
y1 = 0
t1 = 0
ans = True
for i in range(n):
    num = abs(x[i]-x1)+abs(y[i]-y1)
    x1 = x[i]
    y1 = y[i]
    t1 = t[i]-t1
    if num == 0 :
        if t1 % 2 != 0:
            ans = False
    else :
        if t1 % num != 0 :
            ans = False
    if ans == False :
        break
    t1 = t[i]
if ans :
    print("Yes")
else :
    print("No")

