T = int(input())

for i in range(1, T+1):
    a,b = map(int, input().split())
    sum = a+b
    print("Case #"+str(i)+": "+str(sum))

# +로 할 때는 문자형이 맞아야 함으로 str 끼리 맞춰주기