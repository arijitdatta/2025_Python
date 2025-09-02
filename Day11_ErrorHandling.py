try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


try:
    result = int("abc")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

myList=[]
myList.append(10)
myList.append('Hello')
myList.append(3.14)

try:
    print(myList[3])  # This will raise an IndexError
except IndexError:
    print("Error: List index out of range.")
