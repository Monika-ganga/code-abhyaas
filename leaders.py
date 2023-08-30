a=[10,22,12,3,0,6]
i=len(a)-1
maximum=a[i]
ans=[]
while i>0:
    if(a[i]>=maximum):
        maximum=a[i]
        ans.append(a[i])
    i=i-1
print(ans)
        
    
