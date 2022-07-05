# 파이썬에서 정규 표현식을 지원하는 모듈은 re 모듈
# re.compile("문자열")로 리턴받은 패턴 객체로 작업을 수행

import re

p = re.compile("[a-z]+")

# 문자열 검색(match(), search(), findall(), finditer())
# match()와 search()는 매치되는 경우 match 객체를 리턴하며 매치되지 않으면 None을 리턴
# 1. match()
# 문자열의 처음부터 정규식과 매치되는지 조사

# m = p.match("python")
# print(m)   # python
#
# m = p.match("pyt3hon")
# print(m)   # pyt
#
# m = p.match("3 python")
# print(m)   # None
#
# m = p.match("python 3")
# print(m)   # python


# 2. search()
# 문자열 전체를 검색해 정규식과 매치되는지 조사
# m = p.search("python")
# print(m)   # python
#
# m = p.search("python 3")
# print(m)   # python
#
# m = p.search("pyt3hon")
# print(m)   # pyt
#
# m = p.search("3 python")
# print(m)   # python


# 3. findall()
# 정규식과 매치되는 모든 문자열을 리스트로 리턴
# result = p.findall("life is too short")
# print(result)   # ["life", "is", "too", "short"]


# 4. finditer()
# 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴
# result = p.findall("life is too short")
# print(result)   # ["life", "is", "too", "short"]지만 반복 가능한 객체인 iterator object를 리턴


# match 객체의 메서드(group(), start(), end(), span())
m1 = p.match("python")
m2 = p.search("3 python")

# 1. group()
# 매치된 문자열을 리턴
# tmp = m1.group()
# print(tmp)   # python
# tmp = m2.group()
# print(tmp)   # python


# 2. start()
# 매치된 문자열의 시작 위치를 리턴
# tmp = m1.start()
# print(tmp)   # 0으로 int형
# tmp = m2.start()
# print(tmp)   # 2로 int형


# 3. end()
# 매치된 문자열을 끝 위치를 리턴
# tmp = m1.end()
# print(tmp)   # 6으로 int형
# tmp = m2.end()
# print(tmp)   # 8로 int형


# 4. span()
# 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴
# tmp = m1.span()
# print(tmp)   # (0, 6)으로 tuple형
# tmp = m2.span()
# print(tmp)   # (2, 8)으로 tuple형


# p = re.compile("[a-z]+")   m = p.match("python)을 m = re.match("[a-z]+", "python")으로 축약 가능


# 컴파일 옵션(DOTALL(S), IGNORECASE(I), MULTILINE(M), VERBOSE(X))
# 1. DOTALL, S
# 메타 문자 DOT(.)는 \n을 제외한 모든 문자와 매치를 의미하는데 \n을 포함하여 매치하고 싶을때 사용
# p = re.compile("a.b")
# m = p.match("a\nb")
# print(m)   # None을 리턴
# p = re.compile("a.b", re.DOTALL)   # re.S도 가능
# m = p.match("a\nb")
# print(m)   # "a\nb"를 리턴


# 2. IGNORECASE, I
# 대소문자 구별하지 않을때 사용
# p = re.compile("[a-z]+", re.IGNORECASE)   # re.I도 가능
# m = p.match("python")
# print(m)   # "python"을 리턴
# m = p.match("PYTHON")
# print(m)   # "PYTHON"을 리턴


# 3. MULTILINE, M
# 메타 문자 ^와 &를 문자열 전체가 아닌 각 라인마다 적용해주는 것
# data = """python one
# life is too short
# python two
# you need python"""
# p = re.compile("^python\s\w+")
# tmp = p.findall(data)
# print(tmp)   # ["python one"]을 리턴
# p = re.compile("^python\s\w+", re.MULTILINE)  # re.M도 가능
# tmp = p.findall(data)
# print(tmp)   # ["python one", "python two"]를 리턴



# 백슬래시(\)
# \가 포함된 문자 \section을 찾기위해 정규식을 \section으로 만들면 \s가 공백 문자로 인식되는 오류가 발생
# 그러므로 \\section으로 변경해야하지만 파이썬 정규식 엔진에서 \\를 \로 변경하기때문에 \\\\section을 사용해야함
# 컴파일해야하는 정규식이 Raw String을 표시하기위해 r을 앞에 붙여 사용
# p = re.compile(r"\\section")은 \section을 컴파일



# sub
# 정규식과 매치되는 부분을 다른 문자로 바꿀 수 있음
# p = re.compile("(blue|white|red)")
# tmp = p.sub("color", "blue socks and red shoes")   # 첫번째 매개변수는 바꿀 문자열이며 두번째 매개변수는 대상이 되는 문자열
# print(tmp)   # "color socks and color shoes" 리턴
# tmp = re.sub("(blue|white|red)", "color", "blue socks and red shoes")   # 한 문장으로 축약 가능
# print(tmp)   # "color socks and color shoes" 리턴
# tmp = re.sub("(blue|white|red)", "color", "blue socks and red shoes", count=1)   # count 옵션으로 바꾸려는 횟수 설정 가능
# print(tmp)   # "color socks and red shoes" 리턴

