a=[1,-3,6,5,-2,-8]
print(a)
arr=[0]*len(a)
positive=0
negative=1
for i in range(len(a)):
    if(a[i]>0):
        arr[positive]=a[i]
        positive=positive+2
    else:
        arr[negative]=a[i]
        negative=negative+2
print(arr)
    
