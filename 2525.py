h, m = map(int, input().split())
t = int(input())
x = m+t
if x < 60 :
    print(h, x)

elif x >= 60 :
    h += 1
    x = x%60
    if h <= 23 :
        print(h, x)
    elif h >=24 :
        h = h%24
        x = x%60
        print(h, x)