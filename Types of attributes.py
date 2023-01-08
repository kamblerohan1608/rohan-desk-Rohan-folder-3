
# Types Of Attributes : 

# 1. Instance attribute (Used with self) : 

#      Instance attribute carries different behaviour with objects.(attributes with self are instance attribute)

# e.g.
print("****** Instance Attribute ********")
print()
class employee:
    def __init__(self,name):
        self.name = name

o = employee("Rohan")
print(o.name)
o1 = employee("Shiksha")
print(o1.name)

#  2.  Class attribute   <--|
#                           | - - Both are same in python
#  3.  Static attribute  <--|

#       Attributes which carries same behaviour with all objects.(defined in class but not inside any method)

# e.g.
print()
print("********* Class / Static Attribute ************")

class employee:
    company = "Google"
    def __init__(self):
        self.emp_id = 101
        self.emp_loc = "Simla"
    def department(self):
        self.dep_code = 456
        self.dep_loc = "Kerla"

obj = employee()
print(obj.company)

obj1 = employee
print(obj1.company)                 #same behaviour for bothe the objects


employee.company = "Intel"          # changing the class attribute  

print(obj.company)
print(obj1.company)                  # changed for bothe the objects

print()