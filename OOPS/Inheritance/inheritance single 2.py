# single inheritance 3 constructor with parameters

class student:
    def __init__(self,stu_name,stu_roll,stu_loc) :
        self.stu_name = stu_name
        self.stu_roll = stu_roll
        self.stu_loc = stu_loc
    def s1(self):
        print("Student Method 1 accessed")

class employ(student):
    def __init__(self,emp_name,emp_id,emp_salary,stu_name,stu_roll,stu_loc):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        super().__init__(stu_name,stu_roll,stu_loc)

    def e1(self):
        print("Employ Method 1  accessed")

obj = employ("Rohan",102,20000,"Simran",65,"Shrirangpur")
obj.s1()
obj.e1()

print("Employee name is : ",obj.emp_name)
print("Employee id is : ",obj.emp_id)
print("Employee salary is : ",obj.emp_salary)
print("Student name is : ",obj.stu_name)
print("Student roll no. is : ",obj.stu_roll)
print("Student location is : ",obj.stu_loc)