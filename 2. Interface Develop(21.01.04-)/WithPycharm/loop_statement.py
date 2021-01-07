

# 주어진 문장에서 모든 문자를 대문자로 출력한다면?
# 놓침

# break, continue
# search = 17
search = 17
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == search:
        continue
        print('Found -', num)
        #break
    else:
        print('Not Found -', search)

# for ~ else
search = 5
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == search:
        print('Found -', num)
        break
else:
    print('Not Found -', search)



for j in range(1,6):
    for j in range(1, 4):
        print('i - {}, j - {}'.format(i,j))


for i in range(2,10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, (i*j)), end='\t')
    print()
    if i == 5:
            break

string ='''동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리 나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 나라 사랑하세'''
sentences = []
words = []

# append(), insert(), extend()
for s in string.split('\n'):
    sentences.append(s)
    for w in s.split():
        words.append(w)
print('sentences - ', sentences, len(sentences))
print('word      - ', words, len(words))


# 분류정확도
answer = [1, 0, 2, 1, 0]
predict = [1, 0, 2, 0, 0]
acc = 0
for idx in range(len(answer)):
    fit = answer[idx] == predict[idx]
    # print(int(fit), end ='\t')
    acc += int(fit) * 20

print('classification accuracy -', acc)


'''
enumerate
반목문 사용시 몇 번째 반복문인지 확인이 필요하다면
인덱스 번호와 컬렉션 요소를 확인할 수 있다
'''

booklist = ['SQL', 'R', 'TEXT-MINING', 'NLP', 'DATA-MINING', 'PYTHON', 'DJANGO']
for idx, book in enumerate(booklist):
    print('index - {}, value = {}'.format(idx, book))

'''
syntax)
while <expression>:
    statement
    증감식
'''

cnt = 5
while cnt > 0:
    print(cnt)
    cnt = cnt - 1
    print('cnt -', cnt)

# list - pop()
whilelist = ['boo', 'zoo', 'soo']
while whilelist:  # 이건 while True라는 의미
    print(whilelist.pop())   # 이렇게 해서 리스트가 비면 False가 되니까
    print('whilelist - ', whilelist)
print('while - end')



# 난수를 발생시켜

import random
ran = random.random()  # 0~1 사이의 난수를 발생시키는데(실수형)
print('random -', ran)

'''
숫자 범위 : 1~10
내가 입력한 숫자 > 난수: 더 작은 수 입력
내가 입력한 숫자 < 난수: 더 큰 수 입력
'''
rand_num = random.randint(1, 10)
while True:
    guess_num = int(input('예상 숫자를 입력하세요: '))
    if rand_num == guess_num:
        print('success')
        break
    elif rand_num > guess_num:
        print('더 큰 수를 입력하세요')
    else:
        print('더 작은 수를 입력하세요')


'''
>>>> GuessGAME
1 ~ 100 사이의 난수를 발생시킨다
도전횟수는 20회 제한
출력 결과로는
> 정답 시도횟수
> 정답
'''

### 다시 확인하기 ###

from random import randint

rand_num = random.randint(1, 101)  ## randint에서 (a, b) b 숫자를 포함?
try_times = 1
while try_times <= 20:
    guess_num = int(input('예상 숫자를 입력하세요: '))
    if rand_num == guess_num:
        print('success')
        break
    elif rand_num > guess_num:
        print('더 큰 수를 입력하세요')
    elif rand_num < guess_num:
        print('더 작은 수를 입력하세요')
    try_times += 1
if guess_num == rand_num:
    print('정답 시도횟수 {}'.format(try_times))
    print('정답 {}'.format(rand_num))
else:
    print('정답 {}'.format(rand_num))




# random choices()
dataset = list(range(1, 10001))
print(dataset)

# 모집단 dataset에서 k개의 데이터를 샘플링하고 싶다면?
train = random.choices(dataset, k = 10)
print('sample dataset -', train)
