import math


# 소수 판별할 때 N의 제곱근까지만 확인하면 시간 복잡도는 O(N)에서 O(N^(1/2))로 감소

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


# 에라토스테네스의 체
# N보다 작거나 같은 모든 소수를 찾을 때 사용
# 시간 복잡도는 O(NloglogN)으로 선형 시간에 가깝지만 메모리가 많이 필요하다는 단점이 있음

# 1. 2부터 N까지 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
# 3. 남은 수 중에서 i의 배수를 모두 제거(i는 제거하지 않음)
# 4. 반복할 수 없을 때까지 2번, 3번 과정을 반복


n = 1000   # 2부터 1000까지의 모든 수에 대해 소수 판별
arr = [True for i in range(n + 1)]   # 처음엔 모든 수가 소수라고 초기화(0, 1은 제외)

for i in range(2, int(math.sqrt(n)) + 1):   # 에라토스테네스의 체 알고리즘
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(2, n + 1):
    if arr[i]:
        print(i, end=" ")


