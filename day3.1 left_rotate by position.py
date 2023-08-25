a=[3,6,7,9,11,12]
print(a)
k=2
i=0
j=len(a)-1
def left_array(i,j):
    while(i<j):
        a[i],a[j]=a[j],a[i]
        i=i+1
        j=j-1
    return a
left_array(0,k-1)
left_array(k,len(a)-1)
left_array(0,len(a)-1)
print(a)
    
