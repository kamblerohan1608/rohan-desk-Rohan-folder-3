# inheritance multi level constructor with parameter

class student:
    def __init__(self,stu_name,stu_roll,stu_marks,stu_contact):
        self.stu_name = stu_name
        self.stu_roll = stu_roll
        self.stu_marks = stu_marks
        self.stu_contact = stu_contact

class employ(student):
    def __init__(self,emp_name,emp_id,emp_salary,emp_location,stu_name,stu_roll,stu_marks,stu_contact):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_location = emp_location
        super().__init__(stu_name,stu_roll,stu_marks,stu_contact)

class company(employ):
    def __init__(self,com_name,com_sector,com_loc,com_rank,emp_name,emp_id,emp_salary,emp_location,stu_name,stu_roll,stu_marks,stu_contact):
        self.com_name = com_name
        self.com_sector = com_sector
        self.com_loc = com_loc
        self.com_rank = com_rank
        super().__init__(emp_name,emp_id,emp_salary,emp_location,stu_name,stu_roll,stu_marks,stu_contact)


obj = company("IBM","IT","Mumbai",6,"Rohan",564,55000,"Chembur","Shubham",12,689,5632145789)
print("Company name is : ",obj.com_name)
print("Employee name is :",obj.emp_name)
print("Student name is : ",obj.stu_name)
