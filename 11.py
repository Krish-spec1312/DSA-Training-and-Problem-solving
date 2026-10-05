arr={}
arr[1]=1
arr['1']=2
arr[1]+=1
print(arr)
sum=0 
for k in arr:
    sum+=arr[k]
print(sum)
