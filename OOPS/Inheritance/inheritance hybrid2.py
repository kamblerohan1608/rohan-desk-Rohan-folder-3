# Constructor with parameter

class company:
    def __init__(self,com_name):
        self.com_name = com_name

class developer(company):
    def __init__(self,dev_req,com_name):
        self.dev_req = dev_req
        super().__init__(com_name)

class tester(company):
    def __init__(self,test_req,dev_req,com_name):
        self.test_req = test_req
        super().__init__(dev_req,com_name)

class project(tester,developer):
    def __init__(self,pro_name,test_req,dev_req,com_name):
        self.pro_name = pro_name
        super().__init__(test_req,dev_req,com_name)


obj = project("automation Anywhere",11,5,"vipro")
print("Company names : ",obj.com_name)
print("Project name is : ",obj.pro_name)
print("Developers required : ",obj.dev_req)
print("Testers required : ",obj.test_req)