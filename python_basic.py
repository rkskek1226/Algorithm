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






