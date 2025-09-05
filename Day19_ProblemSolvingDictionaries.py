# Problem 1: There is a list l1=[1,2,2,3,2,4,5,5,6,7,8,8,9]. Write a Python program to create a dictionary that contains the frequency of each element in the list.
# Solution:
l1 = [1, 2, 2, 3, 2, 4, 5, 5, 6, 7, 8, 8, 9]
frequency_dict = {}
for item in l1:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1
print("Prob 1: Frequency of each element in the list:", frequency_dict) 


#Side note - how to create a dictionary from a list
l2=['apple', 'banana', 'cherry']
dictionary={}
dictionary[l2[0]]=1

print(dictionary) # Output = {'apple': 1}

# Problem 2: There is a list l1=[1,2,2,3,2,4,5,5,6,7,8,8,9]. Write a python program to count the most repitive element in the list.
# Solution:
l1 = [1, 2, 2, 3, 2, 4, 5, 5, 6, 7, 8, 8, 9]
freqDict = {}
for item in l1:
    if item in freqDict:
        freqDict[item] += 1
    else:
        freqDict[item] = 1
most_repetitive_element = max(freqDict, key=freqDict.get)
print("Problem2: Most repetitive element in the list:", most_repetitive_element)


