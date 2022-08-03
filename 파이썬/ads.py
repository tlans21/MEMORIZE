import math

def add(a,b): #덧셈 함수
     return a+b 
def sub(a,b): #뺄셈 함수
     return a-b 
def div(a,b): #나눗셈 함수
    if(b!=0): 
        return a/b 
def mul(a,b): #곱셈함수 
    return a*b
def remain(a,b): #나머지
    return a % b
def pow_1(a,b) : #승수구하기
    return math.pow(a,b)
def run(): 
    while True:  
        dict = {'1' : '덧셈','2':'뺄셈','3':'나눗셈','4':'곱셈','5':'나머지','6':'승수구하기','7':'종료'}
        print(dict)
        menu=int(input("메뉴 선택>>>"))
        
        if(menu==1): 
            a,b=map(int,input("두 정수 입력:").split())
            print("%d + %d = %d"%(a,b,add(a,b))) #덧셈함수 호출

        elif(menu==2):
             a,b=map(int,input("두 정수 입력:").split()) 
             print("%d - %d = %d"%(a,b,sub(a,b))) #뺄셈함수 호출 
             
        elif(menu==3):
            a,b=map(int,input("두 정수 입력:").split()) 
            if(b==0): 
                print("0으로 나눌 수 없습니다.") #0으로 나눌때 
            else:
                print("%d / %d = %0.2f"%(a,b,div(a,b))) #나눗셈 함수 호출 

        elif(menu==4): 
            a,b=map(int,input("두 정수 입력:").split()) 
            print("%d * %d = %d"%(a,b,mul(a,b))) #곱셈함수 호출 

        elif(menu==5):
            a,b=map(int,input("두 정수 입력:").split()) 
            print("%d * %d = %d"%(a,b,remain(a,b))) #나머지
        elif(menu==6):
            a,b=map(int,input("두 정수 입력:").split()) 
            print("%d * %d = %d"%(a,b,pow_1(a,b))) #승구하기
        elif(menu==7):
            print("종료")
            break


            
if __name__=="__main__": run() #run함수 호출

