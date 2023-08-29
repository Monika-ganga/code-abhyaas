a=[2,5,6,8,11]
i=0
j=len(a)-1
target=14
a.sort()
print(a)
while(i<j):
    current_sum=a[i]+a[j]
    if(current_sum==target):
        print("pair found:",(a[i],a[j]))
        i=i+1
        j=j-1
    elif(current_sum<target):
        i=i+1
    elif(current_sum>target):
        j=j-1
    
    

