

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

booklist = ['SQL', 'R', "TEXT-MINING', 'NLP', 'DATA-MINING', 'PYTHON', 'DJANGO']
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