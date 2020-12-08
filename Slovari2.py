s = input().lower().split()

s_clr = set(s)
cnt = int()

for i in s_clr:
    print(i , s.count(i))

#print(s)
#print(s_clr)