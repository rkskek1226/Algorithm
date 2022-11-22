# 리스트의 문자열 원소들을 int형으로 변환하는 방법
# 1. map 사용
str_arr = ["1", "2", "3"]
int_arr = list(map(int, str_arr))
print(int_arr)

# 2. list comprehension
str_arr = ["1", "2", "3"]
int_arr = [int(i) for i in str_arr]
print(int_arr)


# 리스트의 int형 원소들을 문자열로 변환하는 방법
# 1. map 사용
int_arr = [1, 2, 3]
str_arr = list(map(str, int_arr))
print(str_arr)

# 2. list comprehension
int_arr = [1, 2, 3]
str_arr = [str(i) for i in int_arr]
print(str_arr)


# 리스트의 int형 원소들을 단일 값으로 병합하는 방법
int_arr = [1, 2, 3]
a = "".join(map(str, int_arr))
print(a)


# 제곱수의 약수의 개수는 홀수
# 제곱수가 아닌 두 수의 약수 개수는 짝수


# 리스트 2개의 원소들을 더하기
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [a + b for a, b in zip(l1, l2)]
print(l3)


# 아스키코드 변환 함수(ord(), chr())
# A가 65, a가 97
tmp1 = ord("a")   # a의 아스키코드 값을 반환
tmp2 = chr(tmp1)   # 아스키코드 값을 문자열로 반환


# strip(), lstrip(), rstrip()은 특정 문자 제거
tmp1 = "     hello"
tmp1 = tmp1.strip()   # 공백 제거
print(tmp1)

tmp2 = "aaahello"
tmp2 = tmp2.lstrip("a")
print(tmp2)

tmp3 = "helloaaa"
tmp3 = tmp3.rstrip("a")
print(tmp3)


# 대소문자 관련
s = "Hello"
l = s.lower()   # 소문자로 변환
print(l)
u = s.upper()   # 대문자로 변환
print(u)

print(s.islower())   # 소문자인지 확인
print(s.isupper())   # 대문자인지 확인


# 문자열 교체
s = "hello world"
s = s.replace("hello", "hell")
print(s)


# 변수 스왑
# 다중 할당 방식
a = 10
b = 20
a, b = b, a

# 숫자형인 경우 사용 가능한 방식
a += b
b = a - b
a -= b

