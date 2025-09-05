#Lets say we have a list L1 = [1, 2, 2, 3, 2, 3, 4, 5], now identify the most repetitive element in the list?


l1 = [1, 2, 2, 3, 2, 3, 4, 5]
frequency_dict = {}
for item in l1:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

most_repetitive_element = max(frequency_dict, key=frequency_dict.get)
print("Most repetitive element in the list is:", most_repetitive_element)