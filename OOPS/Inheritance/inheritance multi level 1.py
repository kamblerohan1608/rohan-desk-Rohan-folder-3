# inheritance multi level without parameters
'''
class student:
    def A(self):
        self.one = "This is student class method A"
    def B(self):
        self.A()
        return [self.one,"Method B accessed"]

class employ(student):
    def C(self):
        self.two = "This is class employ method C"
    def D(self):
        self.C()
        return [self.two,"Method D assessed"]

class company(employ):
    def E(self):
        self.three = "This is class company method E"
    def F(self):
        self.E()
        return [self.three,"Method F accessed"]
    def G(self):
        self.all = [self.B(),self.D(),self.F()]
obj = company()
print(obj.B())
print(obj.D())
print(obj.F())
obj.G()
print(obj.all)
'''

# inheritance multi level constructor without parameter

class student:
    def __init__(self):
        self.stu_name = "Rohan"
        self.stu_roll = 56
        self.stu_marks = 564
        self.stu_contact = 56322478956
    
class employ(student):
    def __init__(self):
        self.emp_name = "Kamal"
        self.emp_salary = 35000
        self.emp_contact = 56987413655
        self.emp_location = "Palava"
        super().__init__()
class company(employ):
    def __init__(self):
        self.com_name = "IBM"
        self.com_sector = "IT"
        self.com_brance = "Thane"
        self.com_rank = 5
        super().__init__()

obj = company()
print("Company name is : ",obj.com_name)
print("Employee name is : ",obj.emp_name)
print("Student name is : ",obj.stu_name)