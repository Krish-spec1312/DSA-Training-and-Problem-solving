class Students:
    def __init__(self,name,mobileno,emailid):
        self.name = name
        self.mobileno = mobileno
        self.emailid = emailid
    def info(self):
        print("Name : ",self.name)
        print("Mobile Number : ",self.mobileno)
        print("Email ID : ",self.emailid)
Person1 = Students("Kush",9717804261,"24guptak_1@rbunagpur.in")
Person1.info()
