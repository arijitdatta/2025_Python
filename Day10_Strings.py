single_quote_string = 'Hello, Kolkata!'
double_quote_string = "Hello, India!"
triple_quote_string = '''Hello, World!'''

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)

print(single_quote_string[2])  # Accessing character at index 2 

print(single_quote_string[2:5])  # Slicing from index 2 to 4

print(single_quote_string[2:])  # Slicing from index 2 to end

print(single_quote_string * 3)  # Repeating the string 3 times

print(single_quote_string[-1])  # Accessing the last character

print(single_quote_string[::-1])  # Reversing the string

print(len(single_quote_string))  # Length of the string

print(single_quote_string.lower())  # Convert to lowercase

print (single_quote_string+" "+double_quote_string)  # Concatenation

print (single_quote_string in double_quote_string)  # Membership test

print ("Kolkata" in single_quote_string)  # Membership test

print (single_quote_string.isalnum())  # Alphanumeric check
