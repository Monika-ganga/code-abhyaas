a=[1,2,3,4,6,7]
xor=0
maximum=max(a)
print(maximum)
for i in range(1,7):
    xor=xor^i
for i in range(len(a)-1):
    xor=xor^a[i]
print(xor)
