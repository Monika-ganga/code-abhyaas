a=[1,2,3,4,5,7,8]
b=[1,2,3,4,5,6,8,8,9,10]
n1=len(a)
n2=len(b)
union=[]
i=0
j=0
while i<n1 and j<n2:
    if(a[i]<b[j]):
        if(a[i]!=union[-1]):
            union.append(a[i])
        i=i+1
        
    elif(b[j]<a[i]):
        if(b[j]!=union[-1]):
            union.append(b[j])
        j=j+1
        
        
    else:
        union.append(a[i])
        i=i+1
        j=j+1
        
        
while i<n1:
    if(a[i]!=union[-1]):
        union.append(a[i])
    i=i+1
    
    
while(j<n2):
    if(b[j]!=union[-1]):
        union.append(b[j])
    j=j+1
    
print(union)
    
                 
    
    
    
        
