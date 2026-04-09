class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    # Bonus calculate (10% of salary)
    def bonus(self):
        return 0.10 * self.salary

    # Total salary (salary + bonus)
    def total_salary(self):
        return self.salary + self.bonus()

    # Details print karne ka function
    def show(self):
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Bonus:", self.bonus())
        print("Total Salary:", self.total_salary())


# Object create
e1 = Employee("Diwakar", 101, 50000)

# Output
e1.show()