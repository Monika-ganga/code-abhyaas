a=[1,6,9,2,3,5]
second_max=-999
first_max=-999
first_min=999
second_min=999
for i in range(len(a)):
    if a[i]>first_max:
        second_max=first_max
        first_max=a[i]
    if(a[i]>second_max and a[i]!=first_max):
        second_max=a[i]
print("second maximum is:"second_max)
for i in range(len(a)):
    if a[i]<first_min:
        second_min=first_min
        first_max=a[i]
    if(a[i]>second_min and a[i]!=first_min):
        second_min=a[i]
print("second minimum number is:"second_min)

        
