#Define lists
item=[]

#Fill list with data
for x in range(1,11):
    item.append(x)

#Display list contents
print ('Display list contents::')
print(item)

#Display particular list item
print ('Display particular list item::')
print(item[0])
print(item[5])
print(item[9])

#Display the last item of the list - when size is unknown
print ('Display the last item of the list - when size is unknown::')
print(item[-1])

#Define a list with fixed size of 10 elements
fixed_size_list = [0] * 10

#Lists can hold different data types
fixed_size_list[0] = 1 #integer
fixed_size_list[1] = 2.5 #float
fixed_size_list[2] = "Hello" #string
fixed_size_list[3] = True #boolean
fixed_size_list[4] = [1, 2, 3] #list

#Display the last element of the fixed_size_list
print ('Display the last element of the fixed_size_list::')
print(fixed_size_list[4])

#Slicing a list
print
print(fixed_size_list[1:3]) #Display elements from index 1 to 2