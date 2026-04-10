# class person:
#     def __init__(self,name,age):
#      self.__name = name
#      self.age =age
    
#     def greet(self ,name,age):
#         print("hello",self.name)
#         print("your age is",self.age)



# p1 = greet()
# # p1 = person("email",36)
# # p2 = person("ashish",20)
# # p3 = person("aryan" ,16)
# print(p1.name)
# print(p1.age)

# print()

class personal_details:
    def bank_details(self,holder_name,ifsc_code,account_no,amount):
      self.holder_name = holder_name
      self.ifsc_code = ifsc_code
      self.account_no=account_no
      self.amount = amount
      
      print("Holder Name:", self.holder_name)
      print("IFSC Code:", self.ifsc_code)
      print("Account No:", self.account_no)
      print("Amount:", self.amount)

my_obj = personal_details()
my_obj.bank_details("avikesh","sbi0023", "xxxxxxxx3252",20000)