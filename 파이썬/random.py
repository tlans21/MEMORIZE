import random, time



def printMenu(): 
    print('1. 가위')
    print('2. 바위')
    print('3. 보')
    print('4. 종료')

def getmenuNumber():
    playernum = input()

    while playernum not in ['1', '2', '3', '4']:
        print('예시에 나와있는 숫자가 아닙니다.')
        print('다시 입력해주세요.')
        player = input()
    
    return playernum

tool = ['가위', '바위', '보']

while True:
    randoms = random.choice(tool)
    printMenu()
    
    player = getmenuNumber()

    if player == '1':
        if randoms == '가위':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('무승부')
        
        elif randoms == '바위':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('당신이 졌습니다.')
        
        elif randoms == '보':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('당신이 이겼습니다.')

    elif player == '2':
        if randoms == '가위':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('당신이 이겼습니다.')
        
        elif randoms == '바위':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('무승부')
        
        elif randoms == '보':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('당신이 졌습니다.')
    
    elif player == '3':
        
        if randoms == '가위':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('당신이 졌습니다.')
        
        elif randoms == '바위':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('당신이 이겼습니다.')
        
        elif randoms == '보':
            print('상대방이 무얼 낼지 고민하고있습니다.')
            time.sleep(3)
            print('무승부')
    
    elif player == '4':
        break

print('종료되었습니다.')

