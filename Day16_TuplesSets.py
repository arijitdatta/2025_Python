#Creating a tuple 
#Tuple occupies less memory than a list
#Tuple is immutable (cannot be changed)


myTuple=(1, 2, 3, 4, 5)
print(myTuple)
myTuple=("hello", 1.5, 6) #not changing the contents of the tuple—you are reassigning the variable myTuple to a new tuple.
print(myTuple)


#Tuple ops

tp1=(1, 2, 3)
tp2=(4, 5, 6)
print(tp1+tp2) #Concatenation
print(tp1*3) #Repetition
print(len(tp1)) #Length
print(3 in tp1) #Membership
print(tp1[0]) #Indexing
print(tp1[1:3]) #Slicing
print(tp1.index(2)) #Index of element   

#Tuple unpacking
print("Tuple unpacking")
a, b, c = tp1
print(a, b, c)

#Set creation
#Set is unordered and unindexed
#Set is mutable (can be changed)
#Set does not allow duplicate values
print("Set creation")   
mySet={1, 2, 3, 4, 5}
print(mySet)
mySet={"hello", 1.5, 6}
print(mySet)

#How to find the unique elements from a list using set
myList=[1, 2, 2, 3, 4, 4, 5]
print("List:", myList)
mySet=set(myList)
print("Set:", mySet)
myList=list(mySet)
print("List after removing duplicates:", myList)

#Set ops
print("Set operations")
set1={1, 2, 3}
set2={3, 4, 5}
print(set1.union(set2)) #Union
print(set1.intersection(set2)) #Intersection
print(set1.difference(set2)) #Difference
