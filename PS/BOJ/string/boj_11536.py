n = int(input())
l = []

for i in range(n):
    l.append(str(input()))

if l == sorted(l):
    print("INCREASING")
elif l == sorted(l, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")

