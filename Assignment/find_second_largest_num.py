def second_largest(num):
    first_largest=second_largest=0

    for i in num:
        if i<first_largest:
            second_largest=first_largest
            first_largest=i

        elif i>second_largest and i != first_largest:
            second = i


        if second != 0 :
              return second 
        else:
          None

num = [10,5,20,8]

print("second largest number:" ,second_largest(num))