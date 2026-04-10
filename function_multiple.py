# def is_prime(n):
#     if  n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n% i == 0:
#             return False
#     return True

# is_prime ()




# functions_example.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# Calling the functions
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))