# 5주차 알고리즘 과제 퇴사 14501번

n = int(input())

t = []
p = []
dp = [0]*(n+1)

for i in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
    
for i in range(n-1, -1, -1): # 뒤에서 꺼꾸로 채워나감
    if t[i] + i > n: # 상담에 걸리는 시간이 퇴사일 보다 더 클 경우
        dp[i] = dp[i+1] # 다음 날 값 그대로 가져오기
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i]) 
        # 그 날 상담을 안 할 때와 값과, 할 때의 값 중 최대값 선택
        
print(dp[0])


    

 