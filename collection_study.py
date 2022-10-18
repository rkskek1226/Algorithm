import collections


# collections.Counter
c1 = collections.Counter(["qq", "ww", "qq", "ee", "ww"])
print(c1, "\n")

c1["rr"] += 1
print(c1, "\n")

c2 = collections.Counter("hello world")
print(c2)
print(c2["h"], "\n")

del c2["d"]
print(c2, "\n")

print(c2.most_common(2), "\n")


# collections.defaultdit
d1 = collections.defaultdict(int)
print(d1, "\n")

d1["key1"]
print(d1, "\n")

d1["key2"] = "hihi"
print(d1, "\n")

d2 = collections.defaultdict(list)
print(d2, "\n")

d2["key1"]
print(d2, "\n")




