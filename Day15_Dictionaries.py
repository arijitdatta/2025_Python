#Dictionary in Python is a collection of key-value pairs.

#Create an empty dictionary
my_dict = {}

#Adding data to the dictionary
my_dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

#Accessing data from the dictionary
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])

#Change data in the dictionary
my_dict["age"] = 31
print("Updated age:", my_dict["age"])

#print whole dictionary
print(my_dict)  


#Looping through keys
for myKey in my_dict:
    print(f"Key is - {myKey}")

#Looping through values
for myValue in my_dict.values():
    print(f"Value is - {myValue}")

#Looping through key-value pairs
for myKey, myValue in my_dict.items():
    print(f"Key is - {myKey}, Value is - {myValue}")


#How to check if Key is present
key_to_check = input("Enter the key to check: ")
if key_to_check in my_dict: #this line is absolutely important
    print(f"{key_to_check} is present in the dictionary")
else:
    print(f"{key_to_check} is not present in the dictionary")