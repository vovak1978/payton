############ 1 ####################
string = input('Введіть стрічку\n')
number_list = []
for i in string:
    if i.isnumeric():
        number_list.append(i)
print(','.join(number_list))
