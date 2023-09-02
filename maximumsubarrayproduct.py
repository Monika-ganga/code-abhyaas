a=[2,3,-2,4]
n=len(a)
prefix=1
sufix=1
maximum=1
for i in range(len(a)):
    if(prefix==0):
        prefix=1
    if(sufix==0):
        sufix=1
    prefix=prefix*a[i]
    sufix=sufix*a[n-i-1]
    maximum=max(maximum,max(prefix,sufix))
print(maximum)
