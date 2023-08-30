a=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
element=a[0]
n=len(a)
count=1
for i in range(1,len(a)):
    if(a[i]==element):
        count+=1
    else:
        count-=1
        if(count==0):
            element=a[i]
            count=1
print(count)
count1=0
for i in range(len(a)):
    if(a[i]==element):
        count1+=1
print(count1)
if(count1>n/2):
    print(element)
else:
    print(-1)
