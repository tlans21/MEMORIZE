import sys,os,time

def jin():
    print('\t\t\t진달래 꽃')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t김 소 월')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    for i in range(10):
        print()
        time.sleep(1)


def choHon():
    print('\t\t\t진달래 꽃')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t김 소 월')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    for i in range(5):
        print()
        time.sleep(1)


def ummaya():
    print('\t\t\t진달래 꽃')
    time.sleep(1)
    print()
    time.sleep(1)
    print('\t\t\t\t\t김 소 월')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    print('\t진달래 꽃 진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃진달래 꽃')
    time.sleep(1)
    for i in range(20):
        print()
        time.sleep(1)


def printMenu():
    os.system('cls')
    print()
    print()
    print('\t\t\t김소월 시선')
    print()
    print('\t1. 진달래 꽃')
    print()
    print('\t2. 초     혼')
    print()
    print('\t1. 엄마야누나야')
    print()
    print('\t4. 종     료')
    print()
    print('원하는 시를 선택하세요. : ', end='')

def getMenuNumber():
    menuNumber = input()
    while menuNumber not in ['1', '2', '3', '4']:
        print('잘 못 입력하셨습니다. 다시 한 번 입력 부탁드립니다.')
        menuNumber=input()

    return menuNumber

printMenu()
menuNumber = getMenuNumber()
while menuNumber != '4':
    print('\n'*40)
    if menuNumber == '1':
        jin()
    if menuNumber == '2':
        choHon()
    if menuNumber == '3':
        ummaya()
    input('감상 끝났으면 아무 키나 누르세요.')

    printMenu()
    menuNumber=getMenuNumber()

print('나가세요')








