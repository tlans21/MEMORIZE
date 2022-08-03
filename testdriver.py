from Poetry import *
from menu import *
from PoetryBook import *

title='asdsfa'
poet='sdfva'
contents='''dsd
sdds
dssdd
dssdadas
dsdsd
a
dsa
d'''
myPoetryBook=BookOfPoetry()

myPoetry = myPoetryBook.getPoetry(1)
myPoetry.print()
#print(myPoetry.getTitle())
#myPoetry.print()
title ='나의 애송시'
myMenu = Menu(title,myPoetryBook.getTitles())
myMenu.print()
menuNumber=myMenu.getMenuNumber()
while not myMenu.isExit(menuNumber):
    myPoetry=myPoetryBook.getPoetry(menuNumber)
    myPoetry.print()
    myMenu.print()
    menuNumber=myMenu.getMenuNumber()
    


input()



