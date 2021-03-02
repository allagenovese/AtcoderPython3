s = input()
s = s[::-1]
t = ''
for i in s:
    t += i 
    if t == "maerd":
        t = ''
    if t == "remaerd":
        t = ''
    if t == "esare" :
        t = ''
    if t == "resare":
        t = ''
if t == '' :
    print("YES")
else :
    print("NO")

