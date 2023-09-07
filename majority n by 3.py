a=[2,2,1,3,1,1,3,1,1]
count1=0
count2=0
element1=None
element2=None
ans=set()
n=len(a)
for i in range(len(a)):
    if(count1==0 and a[i]!=element2):
        element1=a[i]
        count1=1
    if(count2==0 and a[i]!=element1):
        element2=a[i]
        count2=1
    if(a[i]==element1):
        count1+=1
    if(a[i]==element2):
        count2+=1
    else:
        count1-=1
        count2-=1
major1=0
major2=0
for i in range(len(a)):
    if(a[i]==element1):
        major1+=1
    if(a[i]==element2):
        major2+=1
if(major1>n//3):
    ans.add(element1)
if(major2>n//3):
    ans.add(element2)
print(ans)
