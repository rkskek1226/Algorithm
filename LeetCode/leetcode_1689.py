def minPartitions(self, n: str) -> int:
    cnt = 0

    while int(n) != 0:
        tmp = ""
        for i in n:
            if i == "0":
                tmp += "0"
            else:
                tmp += "1"
        n = str(int(n) - int(tmp))
        cnt += 1

    return cnt