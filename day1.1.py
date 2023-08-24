arr=[1,2,2,3,4,4,5]
dict={}
for i in arr:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
