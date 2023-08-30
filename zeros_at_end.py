a=[1,0,0,1,0,1,0,0,0,1,3]
print(a)
j=len(a)-1
i=0
while(i<j):
    if(a[i]==0):
        a[i],a[j]=a[j],a[i]
        i=i+1
        j=j-1
    elif(a[j]==0):
        j=j-1
    else:
        i=i+1
print(a)
    
