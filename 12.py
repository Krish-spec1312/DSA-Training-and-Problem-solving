my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4
sum=0
for k in my_dict:
    sum += my_dict[k]
print(sum)
