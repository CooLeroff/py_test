s = int(input())
d = {}


def f(n):
    n = n*10
    return(n)

for i in range(s):
    x = int(input())
    if x not in d:
        d[s] = f(x)
        print(f(x))
    else:
        print(d.get(s))
