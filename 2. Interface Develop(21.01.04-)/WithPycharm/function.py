
# python function

'''
함수는 가독성을 높이기 위한 방법으로
하나 이상의 본문을 가지는 코드는 함수로 정의하는 것이 좋다
내장함수 | 사용자정의 함수
함수를 정의할 때는 def 키워드를 이용해서 함수를 정의
'''


# user define function
'''
def return_type function_name(argument)
def function_name() <- 여러개 들어갈 수 있음

def function_name():
    statement
    return value(built-in type)
'''
def user_print():
    print('user_print')

# from digital.python import package_function
# package_function.print_coins()

# from digital.python import package_function as f
#f.print_coins()

#from digital.python.package_function import print_Coins
#print_Coins()

from digital.python import package_function as f

#r_message = f.returnfunc()
#print('call returnfunc() - ', r_message)

e_mesage = f.say_echo('잇룡')
print('call say_echo()-', e_mesage)

domain = f.make_url('naver')
print('call make_url() - ', domain)

f.bad_func('메롱')

tup_rtn = f.tuple_func(1, 2, 3, 4, 5, 6 , 7, 8, 9)
print('call tuple_func() - ', tup_rtn)


f.dict_func(name='sue', age='top secret')

(odd_sum, even_sum) = f.cnt_sum(100, 500)
print('홀수의 합 {}, 짝수의 합 {}'.format(odd_sum, even_sum))


# 인자로 넘겨받은 연도 사이의 윤년을 찾아 리턴시켜주는 함수를 작성한다면?
# list 타입
leapyear_list = f.leapyear_func(1990, 2021)
print('leapyear_list -', type(leapyear_list), leapyear_list)

dict_msg = f.rtn_dict_func(10)
print('dict_msg -', type(dict_msg), dict_msg)