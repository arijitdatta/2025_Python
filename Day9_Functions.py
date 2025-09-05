#Default values
def greet(name, msg="Good morning!"):
    print("Hello", name + "!", msg)


greet("Alice")

#Nested Functions
def say_hello(name):
    def get_message():
        return "Hello " + name + "!"
    return get_message()


result = say_hello("Bob")
print(result)


#Scope and Global Variables
x=100
def print_global_x(x=-1):
    print("Global x:", globals()['x'])
    print("Local x:", x)

print_global_x()