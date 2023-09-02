
a = [-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]
a.sort()  # Sort the input list

ans = []
for i in range(len(a) - 3):
    if i > 0 and a[i] == a[i - 1]:
        continue
    for j in range(i + 1, len(a) - 2):
        if j > i + 1 and a[j] == a[j - 1]:
            continue
        k = j + 1
        l = len(a) - 1
        while k < l:
            s = a[i] + a[j] + a[k] + a[l]
            if s < 0:
                k += 1
            elif s > 0:
                l -= 1
            else:
                ans.append([a[i], a[j], a[k], a[l]])
                k += 1
                l -= 1
                while k < l and a[k] == a[k - 1]:
                    k += 1
                while k < l and a[l] == a[l + 1]:
                    l -= 1

print(ans)

            
    
