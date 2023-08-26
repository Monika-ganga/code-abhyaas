a = [1, 2, 3, 4, 6]
k = 6
maximum_length = 0
i = 0
j = 0
su = 0

while j < len(a):
    su += a[j]
    
    if su == k:
        length = j - i + 1
        maximum_length = max(maximum_length, length)
        
    while su > k:
        su -= a[i]
        i += 1
        
    j += 1

print(maximum_length)

        
        
    
    
