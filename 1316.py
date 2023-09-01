# 그룹 단어 체커

N = int(input())
cnt = N

for _ in range(N):
    S = input()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            continue
        # 알파벳 연속적이지 않고, 알파벳 개수가 2개 이상이면, 그룹 단어 포함 x
        elif S[i] in S[i+1:]: 
            cnt -= 1
            break

print(cnt)