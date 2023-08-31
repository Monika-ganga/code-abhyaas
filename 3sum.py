a=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
ans=[]
for i in range(len(a)):
    if(i>0 and a[i]==a[i-1]):
        continue
    j=i+1
    k=len(a)-1
    while(j<k):
        s=a[i]+a[j]+a[k]
        if(s<0):
            j=j+1
        elif(s>0):
            k=k-1
        else:
            ans.append([a[i], a[j], a[k]])
            j=j+1
            k=k-1
            while(j<k and a[j]==a[j-1]):
                j=j+1
            while(j<k and a[k]==a[k+1]):
                k=k-1
print(ans)
            
    
