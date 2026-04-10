class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def student_details(self ):
        print("student_name:",self.name)
        print("student roll_no:" ,self.roll_no)
        print("student_marks:",self.name)

        

    def pass_fail(self):
        self.marks=marks
        if marks >= 40:
            print("pass:",marks)
        else:
            print("fail:",marks)

name = input("enter your name:")
roll_no =int(input("enter your roll no:"))    
marks = int(input("enter your marks:"))

my_obj = student(name,roll_no,marks)
my_obj.student_details()
my_obj.pass_fail()

