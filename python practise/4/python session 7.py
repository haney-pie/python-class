import random

num_stu = int(input('Enter the number of students: '))
i = 0
min_num = 21
max_num = -1

my_list = []

while i<num_stu:
    x = random.randint(0, 20)
    my_list.append(x) 
    if x<min_num:
        min_num = x
    if x>max_num:
        max_num = x
    i = i+1
    
print(f'My list is: {my_list}')
print(f'Minimum number is: {min_num}')
print(f'Minimum number is the {my_list.index(min_num)}th')
print(f'Maximum number is: {max_num}')
print(f'Maximum number is the {my_list.index(max_num)}th')