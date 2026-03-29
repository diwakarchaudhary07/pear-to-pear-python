# Multiplication Table Project

def multiplication_table(number, limit):
    print(f"{number}  counting table:")
    for i in range(1, limit+1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Function call

multiplication_table(5, 10)
multiplication_table(6, 10)
multiplication_table(7, 10)
multiplication_table(8, 10)
multiplication_table(9, 10)
multiplication_table(10, 10)