arr=[1,2,2,3,4,4,4,5]
dict={}
for i in arr:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
max_occurence=0
for k,v in dict.items():
    if v>max_occurence:
        max_occurence=v
        key=k
print(key,max_occurence)
