def find_common_element(list1,list2):
    common=[]
    for i in list1:
        if i in list2:
            common.append(i)

    return common

list1 = [1,2,3,4]
list2 = [0,2,3,5]
result = find_common_element(list1,list2)
print(result)


