a=[3,4,9,0]
i=len(a)-2
s=a[len(a)-1]
count=1
ans=[]
ans.append(a[len(a)-1])

while(i>=0):
    average=s//count
    if(a[i]>average):
        ans.append(a[i])
    s+=a[i]
    count+=1
    i=i-1
print(ans)

    
