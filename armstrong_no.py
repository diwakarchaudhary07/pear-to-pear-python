# Armstrong number check in Python

num = int(input("Enter a number: "))

# digit count निकालना
order = len(str(num))

# sum of powers
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# check condition
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")