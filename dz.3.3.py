my_list=[4,7,89,5,2,3,5,4]

mid= (len(my_list)+1)//2
first_list=my_list[:mid]
second_list=my_list[mid:]

res_list=[first_list, second_list]
print(res_list)