# 9주차 그리드 알고리즘 과제 동전0 11047번
N, K = map(int, input().split())
coin = []
ans = 0

for i in range(N):
    i = int(input())
    coin.append(i)
    
coin.sort(reverse=True) # 내림차순 정렬

for i in coin:
    ans += K//i
    K = K%i
    
print(ans)