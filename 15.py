box = {}
jars = {}
crates = {}

box['buiscuit'] = 1
box['cake'] = 3

jars['jam'] = 4

crates['box'] = box
crates['jars'] = jars

print(len(crates['box']))
print(len(crates['jars']))