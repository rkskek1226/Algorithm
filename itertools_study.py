import itertools

arr = ["A", "B", "C", "D"]

# 순열
# n개중 r개를 선택(순서 중요)
p = itertools.permutations(arr)
print("itertools.permutations(arr) :", list(p))
p = itertools.permutations(arr, 2)
print("itertools.permutations(arr, 2) :", list(p))


# 조합
# n개중 r개를 선택(순서 중요 X)
c = itertools.combinations(arr, 2)
print("itertools.combinations(arr, 2) :", list(c))


# 중복 조합
# n개중 r개를 중복해서 선택(순서 중요 x)
c = itertools.combinations_with_replacement(arr, 2)
print("itertools.combinations_with_replacement(arr, 2) :", list(c))


# 데카르트 곱(cartesian product)
arr1 = ["A", "B", "C", "D"]
arr2 = ["1", "2", "3", "4"]
arr3 = [arr1, arr2]
p = itertools.product(arr1, arr2)
print("itertools.product(arr1, arr2) :", list(p))
p = itertools.product("ABCD", "1234")
print("itertools.product(\"ABCD\", \"1234\") :", list(p))
p = itertools.product(*arr3)
print("itertools.product(*arr3) :", list(p))