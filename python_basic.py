import collections

# 스네이크 케이스를 사용( apple_price )

# 타입 명시하는 방법
a: str = "1"
b: int = 1


def sample1(c: int) -> bool:
    print(c)
    return True


# 리스트 컴프리헨션(List Comprehension) : 기존의 리스트를 기반으로 새로운 리스트를 만들어냄(딕셔너리도 가능)
d = [n * 2 for n in range(1, 11) if n % 2 == 1]


# iterable 객체 : 반복 가능한 객체로 list, dict, set, tuple, range가 있음
# list는 iterable하지만 iterator 객체는 아님
# iterator는 값을 차례대로 꺼낼수 있는 객체
# iter()로 iterator 객체를 생성하며 next()로 다음 값이 출력됨(마지막에는 StopIteration 예외 발생)
e = iter([1, 2, 3])
print(next(e))
print(next(e))
print(next(e))
print(next(e))   # StopIteration 예외 발생


# generator : iterator를 생성해주는 함수로 yield 키워드 사용
def sample2():
    yield 1
    yield 2
    yield 3


gen = sample2()
print(next(gen))
print(next(gen))
print(next(gen))


# enumerate : 순서가 있는 자료형(list, tuple 등)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체로 리턴하는 함수
f = [1, 2, 3, 4, 5]
for idx, value in enumerate(f):
    print(idx, value)
f = enumerate(f)
print(list(f))


# locals : 로컬 지역의 변수와 값을 딕셔너리 형태로 알려주는 함수
def sample3():
    g = 1
    h = 2
    print(locals())


sample3()


# 비교 연산자 is는 id() 값을 비교하고 ==는 값을 비교함

# mutable object : list, set, dict
# immutable object : bool, int, float, tuple, str

# a = [1, 2]
# a == copy.deepcopy(a)   -> True
# a is copy.deepcopy(a)   -> False

# 리스트에서 append(), pop(), index()는 O(1)
# 리스트에서 del이나 pop(0), min(), max(), reverse()는 O(n)
# 리스트에서 sort()는 O(n logn)
# 리스트에서 sort, reverse()는 자체를 변경하고 None을 리턴
l1 = list()
l2 = []
l3 = [1, 2, 3]
l3.append(4)
l3.insert(3, 5)
del l3[2]   # del은 인덱스 위치에 있는 요소를 삭제
l3.pop(2)   # pop은 인덱스 위치에 있는 요소를 삭제
l3.remove(2)   # remove는 해당 요소를 삭제
try:
    print(l3[5])
except IndexError:
    print("존재하지 않는 인덱스")


# 딕셔너리(파이썬 3.7부터는 입력 순서가 유지됨)
d1 = dict()
d2 = {}
d3 = {"k1": "v1", "k2": "v2"}
d3["k3"] = "v3"
print(d3)
print(d3["k1"])
try:
    print(d3["k4"])
except KeyError:
    print("존재하지 않는 키")

for k, v in d3.items():
    print(k, v)

del d3["k1"]   # 딕셔너리 키 삭제

# defaultdict 객체 : 존재하지 않는 키를 조회할 경우 디폴트 값을 기준으로 해당 키에 대한 아이템을 생성해줌(에러 메세지 출력 X)
d4 = collections.defaultdict(int)
d4["A"] = 1
d4["B"] = 2
d4["C"] += 1

# Counter 객체 : 아이템 갯수를 계산해 딕셔너리로 리턴
tmp = [1, 1, 2, 2, 3, 3, 4, 5, 5, 1, 1]
d5 = collections.Counter(tmp)
print(d5.most_common(3))   # 빈도 수가 높은 요소를 추출

# OrderedDict 객체 : 입력 순서가 유지되는 객체
d6 = collections.OrderedDict({"A": 1, "B": 3, "C": 2})


# isalnum() : 영어나 한글, 숫자로 구성되었으면 True
# isalpha() : 영어나 한글로 구성되었으면 True
s1 = "qwer"
s2 = "q1w2"
print(s1.isalnum())
print(s1.isalpha())


# lambda(익명 함수)
# def 함수이름(매개변수): return 결과   ->   lambda 매개변수: 결과


# sort()는 자체 정렬로 리턴 없음
# a = [3, 4, 1]
# b = a.sort()
# print(a)   # [1, 3, 4]
# print(b)   # None

# sorted()는 정렬 후 리스트로 리턴
# a = [3, 4, 1]
# b = sorted(a)
# c = "zbqsga"
# d = sorted(c)
# e = "".join(sorted(c))   # 정렬 후 다시 문자열로 결합






