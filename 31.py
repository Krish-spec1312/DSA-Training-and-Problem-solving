class Student:
    def __init__(self):
        self.s_name = "Krish"
        self.l_name = "Jha"
        self.s_rollno = 101
        self.s_branch = "CSE"
        self.s_mb = 9096387190

obj = Student()
print(obj.__dict__)