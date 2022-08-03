import sys,time,os

def starrynight():
    print('\t\t\t별 헤는 밤')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t윤 동 주')
    time.sleep(1)
    print("계절이 지나가는 하늘에는 가을로 가득 차 있습니다.")
    time.sleep(1)
    print("나는 아무 걱정도 없이")
    time.sleep(1)
    print("가을 속의 별들을 다 헬 듯합니다.")
    time.sleep(1)
    print("가슴 속에 하나둘 새겨지는 별을")
    time.sleep(1)
    print("이제 다 못 헤는 것은")
    time.sleep(1)
    print("쉬이 아침이 오는 까닭이요")
    time.sleep(1)
    print("내일 밤이 남은 까닭이요")
    time.sleep(1)
    print("아직 나의 청춘이 다 하지 않은 까닭입니다.")
    time.sleep(1)
    print("별 하나에 추억과")
    time.sleep(1)
    print("별 하나에 사랑과")
    time.sleep(1)
    print("별 하나에 씁슬함과")
    time.sleep(1)
    print("별 하나에 동경과")
    time.sleep(1)
    print("별 하나에 시와")
    time.sleep(1)
    print("별 하나에 어머니, 어머니,")
    for i in range(5):
        print()
        time.sleep(1)

def spring():
    print('\t\t\t봄')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t윤 동 주')
    time.sleep(1)
    print("봄이 혈관 속에 시내처럼 흘러")
    time.sleep(1)
    print("돌, 돌 시내 가차운 언덕에")
    time.sleep(1)
    print("개나리, 진달래, 노오란 배추꽃")
    time.sleep(1)
    print("삼동을 참아온 나는")
    time.sleep(1)
    print("풀포기처럼 피어난다.")
    time.sleep(1)
    print("즐거운 종달새야")
    time.sleep(1)
    print("어느 이랑에서나 즐거웁게 솟쳐라")
    time.sleep(1)
    print("푸르른 하늘은")
    time.sleep(1)
    print("아른 아른 높기도 한데......")
    time.sleep(1)

    for i in range(5):
        print()
        time.sleep(1)

def seosi():
    print('\t\t\t\ 서시')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t윤 동 주')
    time.sleep(1)
    print("죽는 날까지 하늘을 우러러")
    time.sleep(1)
    print("한점 부끄럼이 없기를")
    time.sleep(1)
    print("잎새에 이는 바람에도")
    time.sleep(1)
    print("나는 괴로워했다")
    time.sleep(1)
    print("별을 노래하는 마음은")
    time.sleep(1)

    for i in range(5):
        print()
        time.sleep(1)

def printMenu():
    os.system('cls')
    print()
    print()
    print('\t\t\t윤동주 시선')
    print()
    print('\t1. 별 헤는 밤')
    print()
    print('\t2. 봄')
    print()
    print('\t3. 서 시')
    print()
    print('\t4. 종     료')
    print()
    print('원하는 시를 선택하세요. : ', end='')

def getmenuNumber():
    
    menunumber = input()
    while menunumber not in ['1', '2', '3', '4']:
        print('틀린 숫자를 입력하였습니다. 다시 입력해주세요.')
        menunumber = input()
    
    return menunumber

printMenu()

return_value = getmenuNumber()

while return_value != '4':
    print('\n'*40)
    if return_value == '1':
        starrynight()
    
    if return_value == '2':
        spring()
    
    if return_value == '3':
        seosi()
    
    printMenu()
    return_value = getmenuNumber()

print('종료')       
