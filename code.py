
print("Hello, World!")

name = "Alice"
age = 25


if age >= 18:
    print(name, "is an adult.")
else:
    print(name, "is a minor.")


for i in range(5):
    print("Counting:", i)


def greet(person):
    return "Hello, " + person + "!"

print(greet(name))