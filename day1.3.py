a=[1,1,2,2,2,3,3,3,3,4]
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
count=999
key=0
for k,v in dict.items():
    if v<count:
        count=v
        key=k
print(k,count)
        
    
