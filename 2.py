#Write a program to accept three paper marks M1,M2,M3 and calculate total,percentage and check if user is passed in all subjects so print pass else # fail and check if percentage is greater than 65 and user is having one project so print he/she eligible for placement drive esle print not eligible
M1=int(input("Enter Marks :"))
M2=int(input("Enter Marks :"))
M3=int(input("Enter Marks :"))
project = int(input("Enter Number of Projects:"))
print("Total : ", M1+M2+M3)
percent = ((M1+M2+M3)/3.0)
print("Percentage :",percent)
if M1>=40 and M2>=40 and M3>=40:
    print("Pass")
else:
    print("Fail")
if percent > 65 and project >= 1:
    print("Eligible")
else:
    print("Not Eligible")
