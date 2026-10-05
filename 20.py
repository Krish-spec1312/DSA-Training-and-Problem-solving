#NOT COMPLETE RECHECK IT
my_list=[1,2,3,4]
nmy_list=[]
product = 1
for i in range(0,4):
    for k in range(-1,-4,-1):
        if my_list[i] != my_list[k]:
          product *= my_list[k]
          print(my_list[k])
    nmy_list.append(product)
print(nmy_list)
