s = str(input())
result = ""
upper = False

if "_" in s:
    for i in range(len(s)):
        if s[i].isupper():
            result = "Error!"
            break
        else:
            if s[i] == "_" and s[i-1] == "_":
                result = "Error!"
                break
            if s[i] == "_":
                upper = True
            else:
                if upper:
                    result += s[i].upper()
                    upper = False
                else:
                    result += s[i]

else:
    for i in s:
        if i.isupper():
            result += "_"
            result += i.lower()
        else:
            result += i

if s[0].isupper() or s[0] == "_" or s[-1] == "_":
    result = "Error!"

print(result)
