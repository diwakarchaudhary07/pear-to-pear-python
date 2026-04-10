def remove_common_element(list1):
    common=[]
    print("old list =", list1)
    for i in list1:
        if i not in common:
            common.append(i)


    return common 

list1 =[1,2,2,3,4,4]
# list2 =[]
result= remove_common_element(list1)
print("new list=",result)