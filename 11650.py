# 알고리즘 과제 7주차 좌표 정렬하기 11650번
import sys

N = int(sys.stdin.readline()) 

lst = []

for i in range (N):
    x,y = map(int, sys.stdin.readline().split())
    lst.append([x,y])

lst.sort() # 기본 오름차순 정렬

# 만약 두 번째 값을 기준으로 오름차순 정렬 시
# lst.sort(key = lambda x : (x[1], x[0]))

# 만약 두 번째 값을 기준으로 내림차순 정렬 시
# lst.sort(key = lambda x : (-x[1], x[0]))

# 오로지 두 번째 값을 기준으로만 오름차순 정렬하고 싶을 때
# lst.sort(key= lambda x : x[1])
for i in lst:
    print(i[0], i[1])