############ 1 ####################
#string = input('Введіть стрічку\n')
#number_list = []
# for i in string:
#     if i.isnumeric():
#         number_list.append(i)
# print(','.join(number_list))

############# 2 ##################
# string = input('Введіть стрічку\n')
# temp = ''
# for i in string:
#     if i.isdigit() or i.isspace():
#         temp += i
# number_list = list(temp.split(" "))
# print(','.join(number_list))

############# 3 ##################
# string = input('Введіть стрічку\n')
# string_list = []
# for i in string:
#     if i not in string_list:
#         string_list.append(i)
#         print("'",i ,"'",'-> ', string.count(i), sep='')

#################   PART 2  ################################

################### 1 ########################
# greeting = 'Hello, world'
# list1 = [i for i in greeting.upper()]
# print(list1)

###################### 2 #########################
# list1 = [i*i for i in range (50) if i % 2 == 0]
# print(list1)

#################### 3 ##########################
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# list2 = ['GT' if i > 4 else 'LT' for i in numbers]
# print(list2)

################## 4 ############################
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
# list3 = [(i,-i) for i in list1 if -i in list2]
# print(list3)