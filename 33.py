class Student:
    number = 101 # Data Member
    def __init__(self):
        print("I am Constructor")
    def msg(self):
        print("Hello")# Function in class is called method
obj1 = Student()
print(obj1)
obj1.msg()
obj2 = Student()
print(obj2.number)
# To Create Memory and Address it to the object 
# One Object needs only one constructor
# it it used to initialise the obeject
# Constructor is called automatically
