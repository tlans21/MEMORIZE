import os,sys,time

class Menu:
    def __init__(self,title,contents):
        self.title=title
        self.contents=contents
        self.exitNumber=len(self.contents)+1
        self.validNumbers=[str(i+1) for i in range(self.exitNumber)]

    def printCLS(self):
        os.system('cls')
    def printTitle(self):
        print('\t\t' +self.title)
    def printContents(self):
        i=1
        for content in self.contents:
            print(f'\t{i}. {content}')
            print()
            i+=1
        print(f'\t{i}. 종   료')
    def print(self):
        self.printCLS()
        print('\n'*2)
        self.printTitle()
        print('\n'*2)
        self.printContents()
        print('\n'*2)
        print('\t원하는 메뉴를 선택하시오  :', end='')

    def getMenuNumber(self):
        menuNumber = input()
        while menuNumber not in self.validNumbers:
            menuNumber=input('잘못 입력하셨습니다. 다시 입력해주세요. : ')
        return int(menuNumber)
    def isExit(self,menuNumber):
        if menuNumber == self.exitNumber:
            return True
        else:
            return False

        


