a=[2,5,9]
b=[4,6,8]
i=0
j=0
n1=len(a)
n2=len(b)
while i<n1:
    if(a[i]<=b[j]):
        i=i+1
    else:
        a[i],b[j]=b[j],a[i]
        i=i+1
c=b[0]
while i<n2-1:
    b[i]=b[i+1]
    i=i+1
b[len(a)-1]=c


print(a)
print(b)
