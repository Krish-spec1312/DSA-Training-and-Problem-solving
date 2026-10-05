#Write a program to remove duplicates
name = "prashaant"
newname=""
for i  in name:
    if i not in newname:
        newname = newname + i
print(newname)
