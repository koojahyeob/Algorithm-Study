# 알고리즘 과제 5주차  계단오르기 (2579)
n = int(input())

stair = []
d = [0] * n

for _ in range(n):
    stair.append(int(input()))
    
def climbstairs(n):
    if n == 1:
        d[0] = stair[0]
        return d[0]
    elif n == 2:
        d[1] = stair[0] + stair[1]
        return d[1]
    for i in range (2,n):
        d[0] = stair[0]
        d[1] = stair[0]+stair[1]
        d[i] = max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])
    return d[-1]
    
print(climbstairs(n))