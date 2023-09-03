n = int(input())

stair = [] # 계단 리스트 생성
d = [0] * n # dp 초기화

for _ in range(n):
    stair.append(int(input()))
    
def climbstairs(n): # 계단 함수 생성
    if n == 1: # 초기값 지정
        d[0] = stair[0]
        return d[0]
    elif n == 2: # 초기값 지정 2
        d[1] = stair[0] + stair[1]
        return d[1]
    for i in range (2,n): # 점화식 생성
        d[0] = stair[0]
        d[1] = stair[0]+stair[1]
        d[i] = max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])
    return d[-1]
    
print(climbstairs(n))