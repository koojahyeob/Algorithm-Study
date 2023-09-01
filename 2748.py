<<<<<<< HEAD
# 알고리즘 과제 5주차 피보나지 수 2 2748번
n = int(input())

d = [0] * (n+1) # n 까지의 수열 값 저장

def fibo(x):
    if x == 0 : # 종료조건 1
        return 0
    
    if x == 1 or x == 2 : # 종료 조건 2
        return 1

    if d[x] != 0: # 이미 계산한 값이라면 그대로 반환
        return d[x]
    
    # 점화식 생성
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(n))
=======
# 알고리즘 과제 5주차 피보나지 수 2 2748번
n = int(input())

d = [0] * (n+1) # n 까지의 수열 값 저장

def fibo(x):
    if x == 0 : # 종료조건 1
        return 0
    
    if x == 1 or x == 2 : # 종료 조건 2
        return 1

    if d[x] != 0: # 이미 계산한 값이라면 그대로 반환
        return d[x]
    
    # 점화식 생성
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(n))
>>>>>>> 4bb93d60c9fe268bf85ee7c5878c20aa6b0ff503
