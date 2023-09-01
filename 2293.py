# 알고리즘 과제 5주차 동전 1 2293번

n, k = map(int, input().split())

coin = []
dp = [0]*(k+1) # n+1개 생성

for _ in range(n):
    coin.append(int(input()))

dp[0] = 1
for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i] # 점화식 생성 

print(dp[k])