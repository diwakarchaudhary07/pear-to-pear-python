def add(a,b):
    return a+b


def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b ==0:
        return "cant divide by zero"
    return a/b

while True:
    print("\n---calculator----")
    print("1.addition")
    print("2.subtract")
    print("3.multiply")
    print("4.division")
    print("5.Exit")

    choice=input("enter your choice:")

    if choice =="5":
        print("calculator closed")
        break


    num1 = float(input("enter your num1:"))
    num2= float(input("enter your num2:"))
    
    if choice == "1":
        print("result :",add(num1,num2))
    elif choice == "2":
        print("result :",sub(num1,num2))
    elif choice == "3":
        print("result :",mul(num1,num2))
    elif choice == "4":
        print("result :",div(num1,num2))
    else:
        print("invalid choice")