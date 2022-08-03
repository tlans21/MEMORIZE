from Poetry import *
from menu import *
from PoetryBook import *


myPoetryBook=BookOfPoetry()


title ='나의 애송시'
myMenu = Menu(title,myPoetryBook.getTitles())
myMenu.print()
menuNumber=myMenu.getMenuNumber()
while not myMenu.isExit(menuNumber):
    myPoetry=myPoetryBook.getPoetry(menuNumber)
    myPoetry.print()
    myMenu.print()
    menuNumber=myMenu.getMenuNumber()
    


print('안녕히 가세요')



