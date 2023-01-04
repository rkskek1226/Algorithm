def romanToInt(self, s: str) -> int:
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    subtract_dic = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    result = 0

    for i in subtract_dic.keys():
        if i in s:
            result += subtract_dic[i]
            s = s.replace(i, "")

    for i in s:
        result += dic[i]

    return result

