import random
class Baseball:
    def __init__(self) -> None:
        self._ComputerNumbers=list()
        self._userNumbers=list()
        self._strike=0
        self._ball=0
        self._count=0
    def getComputerNumbers(self):
        self._userNumbers.clear()
        self._count=0
        self._ComputerNumbers.clear()
        newNumber = random.randint(0, 9)
        self._ComputerNumbers.append(newNumber)
        newNumber = random.randint(0, 9)
        while newNumber in self._ComputerNumbers:
            newNumber = random.randint(0, 9) #리스타안에 담겨진숫자가 겹치는 것을 방지하기 위함.
        self._ComputerNumbers.append(newNumber)
        newNumber = random.randint(0, 9)
        while newNumber in self._ComputerNumbers:
            newNumber = random.randint(0, 9)
        self._ComputerNumbers.append(newNumber)
    @property
    def ComputerNumbers(self):
        return self._ComputerNumbers
    def _isVaildUserNumber(self, number):
        if not number.isdigit():
            print("숫자가 아닙니다.")
            return False
        elif len(number) != 1 :
            print("숫자 하나만 입력하세요.")
            return False
        elif number in self._userNumbers:
            print("이미 입력한 숫자입니다")
            return False
        else:
            return True

    def getUserNumbers(self):
        newNumber = input('첫번째 숫자를 입력해주세요 : ')
        while not self._isVaildUserNumber(newNumber):
            newNumber = input('첫번째 숫자를 입력해주세요 : ')
        self._userNumbers.append(newNumber)
        while not self._isVaildUserNumber(newNumber):
            newNumber = input('두번째 숫자를 입력해주세요 : ')
        self._userNumbers.append(newNumber)
        while not self._isVaildUserNumber(newNumber):
            newNumber = input('세번째 숫자를 입력해주세요 : ')
        self._userNumbers.append(newNumber)

    def _chcekResult(self, number):
        self._strike = 0
        self._ball = 0
        self._count +=1
        for number in self._ComputerNumbers:
            if str(number) in self._userNumbers:
                if self._ComputerNumbers.index(number) == \
                    self._userNumbers.index(str(number)):
                    self._strike+=1
                else:
                    self.ball+=1
    def printResult(self):
        self._chcekResult()
        print(f'{self._strike} 스트라이크, {self._ball} 볼')
    def isGameOver(self):
        if self._strike == 3:
            print(f'{self._count} 번 만에 성공')
            return True
        else:
            return False



