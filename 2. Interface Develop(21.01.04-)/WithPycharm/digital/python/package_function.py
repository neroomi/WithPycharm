

## package는 모듈의 집합이라고 생각해라


# 매개변수 X, 리턴값 X
def print_coins():
    print('bitcoin')

# 매개변수 X, 리턴값이 O
def returnfunc():
    return '호출한 쪽으로 값이 전달된다'

# 매개변수 O, 리턴값이 O
def say_echo(name):
    return name + '님, 반갑습니다~다~다~'

# 매개변수 여러개 가능
def calculator(op01, operator, op02):
    pass

def make_url(url):
    return "www."+url+".com"

# 매개변수 O, 리턴값이 X

def bad_func(name):
    pass

# 가변인자를 tuple만 받겠다 (*를 사용하면 가변인자의 개수가 상관없음)
def tuple_func(*args):
    result = 0
    for idx in range(len(args)):
        result += args[idx]
    return result


# 가변인자를 dict로만 받겠다
def dict_func(**args):
    for key, value in args.items():
        print('{} = {}'.format(key, value))


# 범위내에 있는 값의 홀, 짝의 합을 구해서 리턴
def cnt_sum(start, end):
    odd = even = 0
    for x in range(start, end+1) :
        if x % 2 == 0:
            even += x
        else:
            odd += x
    return odd, even


# leapyear
def leapyear_func(start, end):
    leapyear = []
    for y in range(start, end+1):
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            leapyear.append(y)
    return leapyear


def rtn_dict_func(x):
    y01 = x * 10
    y02 = x * 20
    y03 = x * 30
    return {'val01': y01, 'val02': y02, 'val03': y03}
