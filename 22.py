lst = [1,1,0,1,1,0,1,1,1,1]

count = 0
cons = 0

for i in lst:
    if i == 1:
        cons += 1
    else:
        if cons > 0:
            count += 1
        cons = 0

if cons > 0:
    count += 1

print(count)