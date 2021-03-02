n, a, b = map(int, input().split())
ans = 0
for i in range(1,n+1):
    num = i
    sum = 0
    while num > 0 :
        sum += num % 10
        num //= 10
    if a <= sum <= b :
        ans += i
print(ans) 