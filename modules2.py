import sys

str_result = list()
for i in sys.argv:
    str_result.append(i)

str_result.pop(0)
str_end = ' '.join(str_result)
print(str_end)





