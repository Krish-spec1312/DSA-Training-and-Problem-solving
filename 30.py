class Student:
    def __init__(self,name,mobile_no,email_id):
        self.name = name
        self.mobileno = mobile_no
        self.emailid = email_id
    def info(self):
        print("My Name is :",self.name)
        print("My Mobile No is :",self.mobileno)
        print("My Email ID is :",self.emailid)
obj = Student("Krish Jha", 9096387190, "24jhak@rbunapgur.in")
obj.info()