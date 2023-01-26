# Chapter1
# Phython Foundation
# Variable

#Basic
n = 700
print(n)
print(type(n))
print()

#Concurrent Declaration
x = y = z = 700
print(x, y, z)
y = 800
print(x, y, z)
print()

#Object References
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력
print(300)
print(int(300))

n = 777
print(n, type(n))

m = n
print(m, n)
n = 888
print(m, n)
print()

# id(identity)확인 : 객체의 고유값 확인
print(id(m))
print(id(n))
print(id(m) == id(n))

x = 100
y = 100
z = 100
print(id(x), id(y), id(z))
print(id(x) == id(y), id(y) == id(z), id(x) == id(z)) # 같은 오브젝트를 참조

# Naming Rule
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates


#Reserved Word
"""
False / def / if / raise
None / del / import / return
True / elif / in / try
and / else / is / while
as / except / lambda / with
assert / finally / nonlocal / yield
break / for / not
class / from / or
continue / global / pass
"""