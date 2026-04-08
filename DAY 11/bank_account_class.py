# 2. Bank Account

# Ek class BankAccount banao jisme:

# account number, name, balance, pin ho

# deposit aur withdraw function ho

# withdraw tabhi ho jab pin correct ho

class bank_account:
    def __init__(self,acc_num,ifsc_code,name,balance,correct_pin):
        self.acc_num =acc_num
        self.ifsc_code =ifsc_code
        self.name = name
        self.__balance = balance
        self.__correct_pin = correct_pin

    def verifaction(self):
        acc_num = (input("enter your acc_mum:"))
        name = input("enter holder name:")
        pin = int(input("enter pin:"))
        if acc_num==self.acc_num and name==self.name and pin==self.__correct_pin:
            print("show bank balance",self.__balance)
        else:
            print("incorrect verifaction!plese try again")

    def deposit(self):
        if self.verifaction():
            amount = int(input("fill deposit balance:"))
            ifsc=input("fill ifsc code:")
            if ifsc==self.ifsc_code :
              self__balance =+ amount
              print("deposit sucessful")
              print("balance:",self.__balance)
            
            else:
                print("invalid ifsc!")
    
    def withdraw(self):
        if self.verifaction():
            amount = int(input("fill withdraw amount:"))
            pin = int(input("enter your pin:"))
            if pin==self.__correct_pin__pin:
                self.__balance-=amount
                print("withdraw sucessful")
                print("balance:",self.__balance)

    def check_balance(self):
        pin = int(input("enter pin:"))
        if pin == self.__correct_pin :
            print("balance:",self.__balance)


acc_num = input("enter orignal acc_num:")
ifsc_code = input("enter orignal ifsc :")
name = (input("enter holder name:"))
balance = int(input("enter balance:"))
correct_pin = int(input("set pin:"))
# my_obj = bank_account(acc_num,ifsc_code,name,balance,correct_pin)
# my_obj.withdraw()


user = bank_account(acc_num,ifsc_code,name,balance,correct_pin)

# Menu
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        user.deposit()
    elif choice == 2:
        user.withdraw()
    elif choice == 3:
        user.check_balance()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")










        


    













