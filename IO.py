with open ('dataset_3363_2.txt', 'r') as rdoc:
    s = rdoc.readline().strip()
num_result_int = int()
result = str()
x = str()
y = str()

for i in s:
    if i.isalpha():
        if y:
            num_result_int = int(y)
        result = result + (x * num_result_int)
        y = str()
        x = i
    else:
        y = y + i

num_result_int = int(y)
result = result + (x * num_result_int)

with open ('file.txt', 'w') as wdoc:
    wdoc.write(result)




