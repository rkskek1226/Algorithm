# 구간 합 계산
# 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 수를 합한 값을 구하는 경우
# 접두사 합(Prefix Sum) 기법을 사용해 구간 합 계산을 수행
# 접두사 합은 맨 앞부터 특정 위치까지의 합을 구해 놓은 것

# 1. N개의 수에 대해 접두사 합을 계산해 새로운 배열 p에 저장
# 2. left, right에 대해 구간 합을 구하면 p[right] - p[left - 1]


n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = []

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 2
right = 4
print(prefix_sum)
print(prefix_sum[right] - prefix_sum[left - 1])


