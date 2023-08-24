a=[1,3,5,7,9,10]
print(a)
temp=a[0]
i=0
while i<len(a)-1:
    a[i]=a[i+1]
    i=i+1
a[len(a)-1]=temp
print(a)
    
    
