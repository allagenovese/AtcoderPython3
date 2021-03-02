n = int(input())
a = list(map(int , input().split()))
ans = 0
while 1 :
    num = 0
    for i in range(n):
        if(a[i] % 2 == 0) : 
            a[i] = a[i]/2
            num += 1
    if num == n :
        ans += 1
    else :
        break
print(ans)
