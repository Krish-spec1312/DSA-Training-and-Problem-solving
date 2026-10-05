class Student:

    rollno = 101
    def __init__(self):
        print("I am constructor i always called first")
    def msg(self):
        print("Hello World")

obj = Student()
obj.msg()
print(obj)
obj2 = Student()
print(obj.rollno)