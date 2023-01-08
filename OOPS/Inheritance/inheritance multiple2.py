#inheritance multiple constructor with parameters

class student:
    def __init__(self,stu_name,stu_roll,stu_marks,stu_contact):
        self.stu_name = stu_name
        self.stu_roll = stu_roll
        self.stu_marks = stu_marks
        self.stu_contact = stu_contact

class employ:
    def __init__(self,emp_name,emp_id,emp_salary,emp_location):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_location = emp_location

class company(student,employ):
    def __init__(self,com_name,com_sector,com_loc,com_rank,stu_name,stu_roll,stu_marks,stu_contact,emp_name,emp_id,emp_salary,emp_location):
        self.com_name = com_name
        self.com_sector = com_sector
        self.com_loc = com_loc
        self.com_rank = com_rank
        super().__init__(stu_name,stu_roll,stu_marks,stu_contact)
        employ.__init__(self,emp_name,emp_id,emp_salary,emp_location)


obj = company("Infosis","IT","Thane",2,"Harsh",40,750,2658794156,"Sky",897,23000,"Panvel")
print("Company name is : ",obj.com_name)
print("Employee name is :",obj.emp_name)
print("Student name is : ",obj.stu_name)
