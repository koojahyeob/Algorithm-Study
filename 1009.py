# 분산처리
# 1차원적으로 생각하여 제곱 형태의 print를 찍으면 시간초과 발생
# 따라서 일일이 하나하나 경우의 수 나눠서 규칙 만들고, 계산

n = int(input()) # 테스트 개수

for i in range(0,n) :   
    A, B = map(int, input().split()) # A^B 형태
    aa = A%10  #나머지 값 게산
    if aa == 0 : 
        print(10)
    elif aa == 1 or aa == 5 or aa == 6 : # 규칙
        print(aa)
    # 4개씩 규칙적으로 나오기 때문에 이 또한 병합 가능
    elif aa == 2 :
        if B%4 == 0 :
           print(6)
        elif B%4 == 1 :            
            print(2)
        elif B%4 == 2 :            
            print(4)    
        elif B%4 == 3 :            
            print(8)
    elif aa == 3 :       
        if B%4 == 0 :
           print(1)
        elif B%4 == 1 :            
            print(3)
        elif B%4 == 2 :            
            print(9)    
        elif B%4 == 3 :            
            print(7)
    elif aa == 4 :       
        if B%2 == 0 :
            print(6)
        else :            
            print(4)
    elif aa == 7 :       
        if B%4 == 0 :
            print(1)
        elif B%4 == 1 :            
            print(7)
        elif B%4 == 2 :            
            print(9)    
        elif B%4 == 3 : 
            print(3)
    elif aa == 8 :       
        if B%4 == 0 :
            print(6)
        elif B%4 == 1 :            
            print(8)
        elif B%4 == 2 :            
            print(4)    
        elif B%4 == 3 : 
            print(2)
    else:
        if B%2 == 0 :
            print(1)
        else :            
            print(9)
    
    