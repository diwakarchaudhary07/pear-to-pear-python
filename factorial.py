def fact():
    x = int(input("enter your num"))
    fact = 1

    for i in range(1 , x+1):
     fact = fact*i
    
    print("factorial" , fact)


fact()