a=int(input("enter a year1:"))
b=int(input("enter a year2:"))
count=0
if(a>b):
    for i in range(a-1,b,-1):
        if(i%4==0 and  i%100!=0):
            count+=1
        if(i%100==0 and i%400==0):
            count+=1
else:
    for i in range(a+1,b):
        if(i%4==0 and i%100!=0):
            count+=1
        if(i%100==0 and i%400==0):
            count+=1
print(count)
        
            



                
                
        
        
    
            
    

        
