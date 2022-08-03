import os,sys,time

class Poetry:
    def __init__(self,title,poet,contents):
        self.title=title
        self.poet=poet
        self.contents=contents
        self.consoleHeight=os.get_terminal_size().lines
        self.upSpeed=0.5
    def printCLS(self):
        print('\n'*self.consoleHeight)
    def printTitle(self):
        print('\t\t\t'+self.title)
        time.sleep(self.upSpeed)
    def printPoet(self):
        print('\t\t\t'+self.poet)
        time.sleep(self.upSpeed)
    def printContents(self):
        for content in self.contents:
            print('\t'+content)
            time.sleep(self.upSpeed)
    def printBlanklLines(self):
        for i in range(self.consoleHeight-len(self.contents)-7):
            print()
            time.sleep(self.upSpeed)
    def print(self):
        self.printCLS()
        self.printTitle()
        print()
        time.sleep(self.upSpeed)
        self.printPoet()
        print()
        time.sleep(0.5)
        self.printContents()
        self.printBlanklLines()
    def getTitle(self):
        return self.title

        

