from random import randint

def random_numbers():

    numbers = []

    while len(numbers) < 3 :
        randnum = randint(0,9)
        if randnum not in numbers:
            numbers.append(randnum)
    
    print("0과 9 사이의 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    return numbers

def guess():
    guessnum=[]

    while len(guessnum) < 3:
        new_num = int(input("{}번째 숫자를 입력해주세요 : ".format(len(guessnum)+1)))
        
        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in guessnum:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            guessnum.append(new_num)
        
    return guessnum
        
def score(random_key, guess_key):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess_key[i] == random_key[i]:
            strike_count +=1
        elif guess_key[i] in random_key:
            ball_count +=1

    return strike_count, ball_count 

answer = random_numbers()
count = 0

while True:
    user_guess = guess()
    s, b = score(answer, user_guess)
    
    print("{}S {}B\n".format(s, b))
    count +=1

    if s == 3:
        break

print("성공. {}번 만에 맞췄습니다.".format(count))

