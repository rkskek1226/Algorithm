import bisect

# bisect 라이브러리는 정렬된 리스트에서 특정 원소를 찾을 때 효과적
# bisect()와 bisect_right()는 같은 기능
# bisect(a, value, lo=0, hi=len(a))
# bisect()와 bisect_right()는 리스트에 value를



arr = [0, 1, 2, 3, 4, 5]
print(bisect.bisect_left(arr, 3))
print(bisect.bisect(arr, 3))
print(bisect.bisect_right(arr, 3))