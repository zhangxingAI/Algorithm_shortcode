s = list(input())
t = list(input())

def max_silm(s, t):
    a, b = 0, 0
    n = min(len(s), len(t))
    for i in range(n):
        if s[i] == t[i]:
            a+=1
        else:
            break
    for i in range(n):
        if s[-1] == t[-1]:
            b+=1
            s = s[:-1]
            t = t[:-1]
        else:
            break

    return a,b

def cj(a,b):
    return a*b
a, b = max_silm(s, t)
s1,t1 = s, t
s1[a] = t1[a]
s2,t2 = s, t
s2[a] = t2[a]
a,b = max_silm(s, t)
a1,b1 = max_silm(s1, t1)
a2,b2 = max_silm(s2, t2)
result = max(cj(a,b), cj(a1,b1),cj(a2,b2))
print(result)
