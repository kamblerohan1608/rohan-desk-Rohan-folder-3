
# Hash A Realation : 

# It is used to access the property of another class without inheriting it. 

# Simply call the other class inside the constructor of this class and you can access property of both the classes 

class A:
    def __init__(self):
        self.name = "Sudhir"
        self.age = "56"
    def personal(self):
        self.hobbie = "reading"
        self.fav_dish = "Panner Pulav"

class B:
    def __init__(self):
        self.emp_id = 564
        self.emp_location = "Pune"
        self.D = A()
    def Professional(self):
        self.emp_designation = "Tele-caller"
        self.emp_salary = 15000

obc = B()
print("Employee location :",obc.emp_location)
obc.Professional()
print("Emoloyee salary :",obc.emp_salary)

print("Name is :",obc.D.name)
obc.D.personal()
print("Hobbie is :",obc.D.fav_dish)