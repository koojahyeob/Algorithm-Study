# 행렬 덧셈
N, M = map(int, input().split())

arr_A = []
arr_B = []

for i in range(N):
    i = list(map(int, input().split()))
    arr_A.append(i)

for j in range(N):
    j = list(map(int, input().split()))
    arr_B.append(j)

for i in range(N):
    for j in range(M):
        print(arr_A[i][j] + arr_B[i][j], end =' ')
    print()