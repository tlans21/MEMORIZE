from Poetry import *


class BookOfPoetry:
    def __init__(self) -> None:
        self.PoetryBook=list()
        self.loadPoetry()
    def loadPoetry(self):
        title = '서시'
        poet = '윤동주'
        contents ='''죽는 날까지 하늘을 우르러
한점 부끄럼이 없기를
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어가는것을 사랑해야지
그리고 나한테 주여진 길을
거러가야겠다.'''
        myPoetry=Poetry(title,poet,contents.split('\n'))
        self.PoetryBook.append(myPoetry)
        title = '진달래 꽃'
        poet = '김소월'
        contents ='''나 보기가 역겨워
가실 때에는
말없이 고이 보내 드리오리다

양변에 약산
진달래꽃
아름 따다 가실 길에 뿌리오리다

가시는 걸음 걸음
놓인 그 꽃을
사뿐히 즈려밟고 가시옵소서

나 보기가 역겨워
가실 때에는
죽어도 아니 눈물 흘리오리다'''
        myPoetry=Poetry(title,poet,contents.split('\n'))
        self.PoetryBook.append(myPoetry)
        title = '별 헤는 밤'
        poet = '윤동주'
        contents ='''계절이 지나가는 하늘에는 가을로 가득 차 있습니다.
나는 아무 걱정도 없이
가을 속의 별들을 다 헤일 듯 합니다

가슴 속에 하나 둘 새겨지는 별을 이제 다 못헤는 것은
쉬이 아침이 오는 까닭이요, 내일 밤이 남은 까닭이요,
아직 나의 청춘이 다하지 않은 까닭입니다.
'''
        myPoetry=Poetry(title,poet,contents.split('\n'))
        self.PoetryBook.append(myPoetry)
        title = '봄'
        poet = '윤동주'
        contents ='''봄이 혈관 속에 시내처럼 흘러
돌, 돌 시내 가차운 언덕에
개나리, 진달래, 노오란 배추꽃
        
삼동을 참아온 나는
풀포기처럼 피어난다
        
즐거운 종달새야
어느 이랑에서나 즐거웁게 소셔라
        
푸르른 하늘은 아른 아른 높기도 한데.....'''
        myPoetry=Poetry(title,poet,contents.split('\n'))
        self.PoetryBook.append(myPoetry)
        title = '공상'
        poet = '윤동주'
        contents ='''내 마음의 답 나는 말없이 이 탑을 쌓고 있다.
명예와 허영 천공에다,
무너질 줄도 모르고,
한층 두층 높이 쌓는다.
        
무한한 나의 공상 그것은 내 마음의 바다,
나는 두팔을 펼쳐서 나의 바다에서
자유로이 헤엄친다
황금,지옥의 수평선을 향하여'''
        myPoetry=Poetry(title,poet,contents.split('\n'))
        self.PoetryBook.append(myPoetry)

    def getPoetry(self,menuNumber):
        return self.PoetryBook[menuNumber-1]
    def getTitles(self):
        return [poetry.getTitle() for poetry in self.PoetryBook]