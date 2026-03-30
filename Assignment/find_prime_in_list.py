def prime_no():
    element = int(input("enter your num:"))
    list =[]
    for i in range (2 ,element ,3):
        list.append(i)
    print(list)

    # list=[10, 7, 3, 8, 11]
 
    for i in list :
        if i > 1:
            for j in range(2 , i):
                if i % j == 0:
                    print("The num" ,i,"is not prime")
                    break
            else:
                print("The num" ,i,"is  prime")    
        else:
            print("The num" ,i,"is not prime")


prime_no()