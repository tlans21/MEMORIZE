from menu import *
from Calculator import *

title='계산기'
contents=['더하기','빼 기', '곱하기','나누기','더하기']
myMenu=Menu(title,contents)
menuNumber=myMenu.getMenuNumber()
while not myMenu.isExit(menuNumber):
    op1=Calculator('첫번째')
    op2=Calculator('두번째')
    if menuNumber ==1:
        print(op1.Plus(op2))
    elif menuNumber ==2:
        print(op1.Minus(op2))
    else:
        print('개발중입니다.')

    input()
    myMenu=Menu(title,contents)
    menuNumber=myMenu.getMenuNumber()

print()
print('\t\t 수고하셨습니다.')
input()    


