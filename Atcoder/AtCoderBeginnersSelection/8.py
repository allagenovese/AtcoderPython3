n, y = map(int , input().split())
a = -1 
b = -1
c = -1
for i in range(n+1):
    for j in range(0, n+1-i):
        k = n-i-j
        if 10000*i + 5000*j + 1000*k == y :
            a = i
            b = j
            c = k
print(a, b, c)

