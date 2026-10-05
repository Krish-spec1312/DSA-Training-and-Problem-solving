class Details:
    def __init__(self,name,age,rollno): # Parameterize Constructor
        self.name = name
        self.age  = age
        self.rollno = rollno

    def info(self):
        print("My name is ",self.name)
        print("My age is ",self.age)
        print("My roll no is ",self.rollno)
Person1 = Details('Kush',20,22)
Person1.info()
