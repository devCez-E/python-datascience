# Chapter2
# 숫자형

############ 파이썬 지원 자료형 ############
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""


############ Data Type ############
_int = 7
_float = 10.0                # 10 != 10.0
_bool = True

_str = "Python"
_list = ["i", "n", "s", "i", "d", "e"]
_dict = {
    "name" : "Machine Learning",
    "version":2.0
}
_tuple = (7, 8, 9)
_set = {7, 8, 9}

print(type(_int))
print(type(_float))
print(type(_bool))
print(type(_str))
print(type(_list))
print(type(_dict))
print(type(_tuple))
print(type(_set))
print()

print(_int)
print(_float)
print(_bool)
print(_str)
print(_list)
print(_dict)
print(_tuple)
print(_set)
print()


############ 숫자형 연산자 ############
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x ** y
"""


############ 형 변환 연습 ############
a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex(True))
print(complex(False))
print()


############ 수치 연산 함수 ############
print(abs(-7))
x,y = divmod(100, 8)
print(x, y)
print(pow(5, 3), 5**3)
print()

# 외부 모듈
import math
print(math.pi)