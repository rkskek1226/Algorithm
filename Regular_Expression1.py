# 정규 표현식(Regular Expression)은 문자열 처리할때 사용하는 기법
# 메타 문자 : 특별한 용도로 사용하는 문자로 ., ^, $, *, +, ?, {}, [], \, |, ()가 있음

import re

# []
# 문자 클래스 []로 만든 정규식은 [] 사이의 문자들과 매치라는 의미
# [abc]는 a, b, c중 한 개의 문자와 매치를 의미로 "a"는 매치하고 "before"도 매치하지만 "dude"는 매치하지 않음

# []안의 문자 사이에 -를 사용하면 범위를 의미
# [a-c]는 [abc]와 동일하고 [0-5]는 [012345]와 동일
# [a-zA-Z]는 알파벳 모두를 의미하고 [0-9]는 숫자 모드를 의미

# 문자 클래스에 ^를 사용하면 반대라는 의미로 [^0-9]는 문자와 매치를 의미

# [\d]는 [0-9]와 동일한 표현식
# [\D]는 [^0-9]와 동일한 표현식
# [\s]는 [ \t\n\r\f\v]와 동일한 표현식으로 공백 문자와 매치를 의미
# [\S]는 [^ \t\n\r\f\v]와 동일한 표현식으로 공백 문자가 아닌 것과 매치를 의미
# [\w]는 [a-zA-Z0-9_]와 동일한 표현식으로 문자, 숫자와 매치를 의미
# [\W]는 [^a-zA-Z0-9_]와 동일한 표현식으로 문자, 숫자가 아닌 문자와 매치를 의미



# Dot(.)
# 줄바꿈 문자(\n)을 제외한 모든 문자와 매치를 의미
# a.b는 a와 b사이에 어떤 문자가 들어와도 매치된다는 의미로 "aab"와 "a0b"는 매치, "abc"는 매치하지 않음

# 문자 클래스인 []에 Dot(.) 메타 문자가 사용되면 이는 문자 .를 의미
# a[.]b는 "a.b"와는 매치, "a0b"는 매치하지 않음



# *
# *는 반복을 의미하며 * 앞에 있는 문자가 반복된다는 의미
# ca*t는 "ct", "cat", "caaat"와 매치
# *는 0번 반복해도 괜찮



# +
# +는 반복을 의미하며 + 앞에 있는 문자가 반복된다는 의미
# *가 0번 반복해도 괜찮지만 +는 1번 이상부터 반복한다는 것을 의미
# ca+t는 "cat", "caaat"와는 매치하지만 "ct"와는 매치하지 않음



# {}
# {}는 반복 횟수를 지정할 수 있으며 {a, b}는 a번부터 b번까지 반복할 수 있다는 것을 의미
# {a, }는 반복 횟수가 a번 이상인 경우이며 {, b}는 반복 횟수가 b번 이하인 경우
# ca{2}t는 "caat"와만 매치되며 ca{2, 4}는 "caat", "caaat", "caaaat"와만 매치됨



# ?
# ?는 {0, 1}를 의미하며 있어도 되고 없어도 되는 것을 의미
# ab?c는 "abc", "ac"와 매치됨



# |
# |는 or과 동일한 의미로 A|B는 A나 B라는 의미로 사용
# p = re.compile("Crow|Servo")
# m = p.match("CrowHello")
# print(m)   # "Crow"를 리턴



# ^
# ^는 문자열의 맨 처음과 일치를 의미
# print(re.search("^ㅣLife", "Life is too short"))   # Life를 리턴
# print(re.search("^Life", "My Life is too short"))   # None을 리턴



# $
# $는 문자열의 마지막과 일치를 의미
# print(re.search("short$", "Life is too short"))   # short를 리턴
# print(re.search("short$", "Life is too long"))   # None을 리턴



# ()
# ()는 그루핑(grouping)을 가능하게 함
# 특정 문자열이 반복되는지를 검사하고싶을때 그루핑을 사용
# m = re.search("(abc)+", "abc0abcabc qq")
# print(m)   # "abc"를 리턴
# m = re.search("(abc)+", "abcabcabc qq")
# print(m)   # "abcabcabc"를 리턴


# group 메서드(match 객체의 메서드)
# group(0)은 매치된 전체 문자열
# group(1)은 첫번째 그룹에 해당하는 문자열
# group(2)는 두번째 그룹에 해당하는 문자열
# group(n)은 n번째 그룹에 해당하는 문자열
# print(m.group(0))   # "abcabcabc"를 리턴
# print(m.group(1))   # "abc"를 리턴

