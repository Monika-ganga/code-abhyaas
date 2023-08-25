a=[1,1,2,2,3,1,1,1,4,1,1,1,1]
count=0
maximum1=1
for i in a:
    if(i==1):
        count+=1
    if (i!=1):
        count=0
    maximum1=max(count,maximum1)
print(maximum1)
        
