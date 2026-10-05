#WAP to accept any single chr and check the entered chr is in upper case lower case, digit or special symbol and acccording to the print msg
chr = input("Enter any character : ")
if chr.isupper():
    print("Upper")
elif chr.islower():
    print("Lower")
elif chr.isdigit():
    print("Digit")
else:
    print("Special")
#OR
ch = ord(input("Enter any character:")) #ord converts character to  ASCII Code 
if ch>=65 and ch<=90:
    print("Upper")
elif ch>=97 and ch<=122:
    print("Lower")
elif ch>=48 and ch<=57:
    print("Digit")
else:
    print("Special")
