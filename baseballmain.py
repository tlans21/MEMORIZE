from baseball import *

myBaseball =  Baseball()
print(myBaseball.ComputerNumbers)
gameStop = 'N'
while gameStop != 'Y':
    myBaseball.getComputerNumbers()
    print(myBaseball.ComputerNumbers)
    myBaseball.getUserNumbers()
    myBaseball.printResult()
    while not myBaseball.isGameOver():
        myBaseball.getUserNumbers()
        myBaseball.printResult()
    gameStop=input('그만 할까요?(Y/N)').upper()
