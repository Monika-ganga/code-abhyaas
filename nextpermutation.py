a=[1,3,2]
i=len(a)-2
while i>=0 and a[i]>=a[i+1]:
    i=i-1
if i==-1:
    print("There is no next permutation")
else:
    j=len(a)-1
    while a[j]<=a[i]:
        j=j-1
    a[i],a[j]=a[j],a[i]
    l=i+1
    r=len(a)-1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
print(a)
