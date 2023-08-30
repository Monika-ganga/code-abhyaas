a=[-2,-3,4,-1,-2,1,5,-3]
ans_start=-1
ans_end=-1
s=0
m=-9999
for i in range(len(a)):
    if(s==0):
        start=i
    s=s+a[i]
    if(s>m):
        m=s
        ans_start=start
        ans_end=i
    if(s<0):
        s=0
print(m)
        
