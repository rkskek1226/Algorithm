import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l.sort()

left, right = 0, len(l) - 1
tmp_hap = abs(l[left] + l[right])
tmp = [l[left], l[right]]

while left < right:
    hap = l[left] + l[right]
    if abs(hap) < tmp_hap:
        tmp_hap = abs(hap)
        tmp = [l[left], l[right]]
        # tmp.append((l[left], l[right]))
        if tmp_hap == 0:
            break

    if hap < 0:
        left += 1
    else:
        right -= 1

print(tmp[0], tmp[1])
