def prime():
    x = int(input("enter your num"))
    n = 0
    for i in range(2,x):
       if x%i ==0:
        n = n+1
    if n==0:
        print("prime")
    else:
        print("not prime")


prime()