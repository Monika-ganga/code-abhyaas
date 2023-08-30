a=[7,1,5,3,8,4]
minimum=a[0]
profit=0
for i in range(1,len(a)):
    cost=a[i]-minimum
    profit=max(profit,cost)
    minimum=min(minimum,a[i])
print(profit)
