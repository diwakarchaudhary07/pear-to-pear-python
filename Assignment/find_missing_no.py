def find_missing_no(num):
    n = len(num)+1
    list2=[]
    sum1 = n*(n+1)//2
    sum2 =sum(num)
    
    for i in range(1,n+1):
        list2.append(i)
    print("new list",list2)
    
    return sum1-sum2

num =[1,2,3,5]
print("old list",num)    
print("missing_num=",find_missing_no(num))   