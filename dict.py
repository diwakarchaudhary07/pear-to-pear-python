# # method = 1
# student = {
#     "name": " abcd",
#     "course":"B.Tech",
#     "age" : 18,

# }
# print("your info :", student)

# # Method =2

# d = dict(a=1,b=2,c=3)
# print(d)


# # Method = 3
# x= dict([("a",1),("b",2)])
# print(x)


# # Method=4
# student_1 = ([("name"," abcd"),("course","BCA"),("age" , 18)])
# print(student_1)




student_3= {
    "name": " abcd",
    "course":"B.Tech",
    "age" : 18,

}

student_3["name"] = "xyz"

print(student_3)
print(student_3.keys())
print(student_3.values())

for i in student_3.keys():
    print(i)

for i,j in student_3.items():
    print(i,j)