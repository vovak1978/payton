############# 1 ################
# def min_three (a,b,c):
#     min_number = min(a,b,c)
#     print(min_number)
#     return min_number

# min_three(7,1,6)

############# 2 ################
# def max_three (a,b,c):
#     max_number = max(a,b,c)
#     print(max_number)
#     return max_number

# max_three(7,1,6)

############# 3 ################
# def max_min_number (*numbers):
#     min_number = min(*numbers)
#     print(max(*numbers))
#     return min_number

# max_min_number(7,1,6,8,8,15,-5)

############# 4 ################
# def make_a_list (*args):
#     print(list(args))    
#     # return list(args)

# make_a_list()

############# 5 ################
# def min_of_list (*args):
#     return min(list(args))

# print(min_of_list(2,6,8,9,-15)) 

############# 6 ################
# number_list = [1,5,8,9,0]

# def sum_elements_of_list ():
#     global number_list
#     return sum(number_list)

# print(sum_elements_of_list()) 

########### 7 ################
# number_list = [1,5,8,9,0]

# def sum_elements_of_list ():
#     global number_list
#     return (sum(number_list) /len(number_list))

# print(sum_elements_of_list()) 

########### 8 ################

def pr(): 
    return 'Hello_boss_!!!'
    def recovery():
        temp = ''
        for i in pr():
            if i != '_':
                temp += i
            else:
                temp += ' ' 
    return recovery

print(pr())    