# Chapter2
# 문자형

str1 = "I am Python"
str2 = 'Python'
str3 = """How are you??"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))


# 빈 문자열
str_empty1 = ''
str_empty2 = str()
print(type(str_empty1), len(str_empty1))
print(type(str_empty2), len(str_empty2))


# Escape
print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')
print('a \tb')
print('a \nb')

str_escape = "Do you have a \"retro games\"?"
print(str_escape)
print()


# 멀티라인 입력 \
str_multi = \
"""
String
Multi Line
Test
"""
print(str_multi)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "apple"
str_o3 = "How are you doing"
str_o4 = "Seoul|Daejeon|Busan|Jinju"
print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)                    # 시퀀스는 in 연산을 사용 가능
print('z' in str_o1)
print()


# 문자열 형변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()

# 문자열 함수
print("Capitalize : ", str_o2.capitalize())
print("Endswith? : ", str_o2.endswith("!"))
print("Replace : ", str_o1.replace("Nice", "Good"))
print("Replace : ", str_o1.replace("thon", "Good"))
print("Sorted : ", sorted(str_o2))
print("split : ", str_o4.split('|'))
print()


# 반복(시퀀스)
str_loop = "Good Boy!"
print(dir(str_loop))    # __iter__
for i in str_loop :
    print(i)