def fudu(s):
    num = 0
    n = len(s)
    for i in range(n):
        for j in range(n-i):
            if s[i+j] == s[j]:
                num += 1
            else:
                break

    return num

s = input()
print(fudu(s))




