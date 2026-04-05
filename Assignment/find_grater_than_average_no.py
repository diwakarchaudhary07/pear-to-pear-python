def find_grater(list):
    sum =0
    average = 0
    num=[]
    lenth =len(list)
    print("lenth =",lenth)
    for i in list: 
        sum =sum+i
    average=sum/lenth
    print("average no",int(average))
    for i in list:
        if i>average:
         num.append(i)
    return num

list = [10,20,30,40]
result= find_grater(list)
print(result)

