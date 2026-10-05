class Hod:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.empid = rollno
    def info(self):
        print("My Name is :",self.name)
        print("My Age is :",self.age)
        print("My Empid is :",self.empid)
obj = Hod("Krish Jha", 21, 1001)
obj.info()