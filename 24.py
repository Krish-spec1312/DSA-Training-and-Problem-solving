list = 'helpforcode'
vowels ='aeiouAEIOU'
vcount = 0
ccount = 0
for i in list:
    if i in vowels:
        vcount += 1
    else:
        ccount += 1
print('vcount',vcount)
print('ccount',ccount)
