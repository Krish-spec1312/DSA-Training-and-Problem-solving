fruit={}
def add(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
add('Apple')
add('Mango')
add('apple')
print(len(fruit))
