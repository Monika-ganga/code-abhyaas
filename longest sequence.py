def longest_element(a):
    n=len(a)
    if n==0:
        return 0
    longest=1
    st=set()
    for i in range(n):
        st.add(a[i])
    for j in st:
        if j-1 not in st:
            count=1
            x=j
            while x+1 in st:
                x=x+1
                count=count+1
                longest=max(longest,count)
    return longest
a=[100,200,1,2,3,4]
ans=longest_element(a)
print("The longest conseecutive sequence is:",ans)
    
