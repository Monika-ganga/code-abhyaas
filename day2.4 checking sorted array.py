a=[5,4,3,2,1]
flag=0
i=0
if(a[0]<a[1]):
    while(i<len(a)-1):
        if(a[i]<a[i+1]):
            i=i+1
        else:
            flag=1
            break
else:
    while(i<len(a)-1):
        if(a[i]>a[i+1]):
            i=i+1
        else:
            flag=1
            break
if(flag==0):
    print("sorted array")
else:
    print("Not a sorted array")
    
        
    
        
        
        
