with open ('dataset_3363_3.txt', 'r', encoding='utf-8') as rdoc:
    s = rdoc.read().strip().lower()

#s = str('aXapXX pTdb TUpZbZp cpaYU apUUdUddU pTdb UdTZcc T baT cpaYU XUcUYcXc cpaYU U TUpZbZp apUUdUddU cpaYU pdY cpaYU bbUZcZZUd cb U T Y UpbdpYpa dZZZ bpadpa UpbdpYpa cbcppa ccbUaUZU T UU ZTp pdpYTYUp pdpYTYUp Zap aXapXX U UYYX pZbT cbcppa cbcppa Uc UXpUbX dpUapYpUp dT ZaadUUp UpaY YYXbdYZ UpaY YYXbdYZ ZbcZa ZbcZa aYb ZbcZa cdZbZpa UpaY cp UYUUdpcYX pdp aXbX TYa pYd TYa TbcYd XU dbTdddYXd Za dbTdddYXd ZZpdZdUba ZZZYdda ZacbpcZY cp TYa dpapYUbc XabYY dpapYUbc bpYc UpaY bbTcZXZb bXpUapp cYY pc YcccpYaX bXUd Za TT Za YpcaaXZZ TT').lower()
list_split = s.split()
new_list = []
a = ()
prev_word = str()
max_count_word = int()
count_word = int()
max_word = int()

for i in list_split:
    new_list.append(i)
a = sorted(new_list)

print(a)
for i in a:
    if i == prev_word:
        count_word += 1
        if count_word > max_count_word:
            max_count_word = count_word
            max_word = i
    else:
        count_word = 0
    prev_word = i


print(max_word, max_count_word+1)

#num_result_int = int(y)
#result = result + (x * num_result_int)

#with open ('file.txt', 'w') as wdoc:
#    wdoc.write(result)




