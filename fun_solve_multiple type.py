
student = {
    "name":"Ashish",
    "Age":20,
    "course":"BTech"
}
# print(student)    #first method to create dictionary


student = dict(name="Ashish",Age=20,course="Btech")
print(student)

# student=dict([("name","Ashish"),("Age",20),("Course","Btech")]) #third Method

# student = {
#     "name":"Ashish",
#     "Age":20,
#     "course":"BTech"
# }
# print(student.get("name"))   #first method to create dictionary
# student["name"]="Arvin"
# print(student.get("name"))
# print(student.keys())
# print(student.values())

# student["Rollno"]=41
# print(student)
# for i in student:
#     print(i)
# for i in student.values():
#     print(i)
# print("Key value together")
# for k,v in student.items():
#     print(k,v)