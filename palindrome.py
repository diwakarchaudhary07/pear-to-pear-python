num = int(input("enter your num"))
num1 = num
x = 0 
l = len(str(num))
for i in range(l):
    rem = num%10
    x = x*10 + rem
    num = num//10

if (x==num1):
    print("palindrome num")
else:
    ("not ! palindrome")

