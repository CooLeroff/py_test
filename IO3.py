x = []
y = float()
sum = int()
f_num = int()
s_num = int()
t_num = int()
l_count = int()

with open("result.txt", "w+") as w:
    with open('dataset_3363_4.txt', 'r', encoding='utf-8') as f:
        for line in f:
            l_count += 1
            x = line.strip('\n').split(';')
            f_num = f_num + int(x[1])
            s_num = s_num + int(x[2])
            t_num = t_num + int(x[3])
            print((round((int(x[1]) + (round(int(x[2])) + int(x[3]))) / 3, 9)), file=w)

with open("result.txt", "a") as w:
    print(round((f_num / l_count), 9), round((s_num / l_count), 9), round ((t_num / l_count), 9), file=w)




