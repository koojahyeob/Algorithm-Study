# EOF 입력이 끝날 때까지 출력

while True :
    try :
        a,b = map(int, input().split())
        print(a+b)
    except :
        break
    