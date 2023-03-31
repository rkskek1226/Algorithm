# 짐을 쪼갤 수 있는 배낭 문제

cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]   # (가치, 무게) 형식

def fractional_knapsack(cargo):
    capacity = 15   # 배낭의 무게
    pack = []

    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)   # 무게 당 가치가 큰 순서대로 정렬

    # 단가 순서대로 그리디 계산
    total_value = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value


