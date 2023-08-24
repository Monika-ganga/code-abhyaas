a=[1,1,2,2,2,3,3,4,4,4,4,5]
i=0
j=i+1
while (j<=len(a)-1):
    if (a[i]==a[j]):
        j=j+1
    else:
        i=i+1
        a[i]=a[j]
a=a[:i+1]
print("removed duplicates array is:",a)
    
    
