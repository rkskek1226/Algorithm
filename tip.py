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


# 제곱수의 약수의 개수는 홀수
# 제곱수가 아닌 구수의 약수 개수는 짝수


# 리스트 2개의 원소들을 더하기
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [a + b for a, b in zip(l1, l2)]
print(l3)


# 아스키코드 변환 함수(ord(), chr())
# A가 65, a가 97
tmp1 = ord("a")   # a의 아스키코드 값을 반환
tmp2 = chr(tmp1)   # 아스키코드 값을 문자열로 반환




