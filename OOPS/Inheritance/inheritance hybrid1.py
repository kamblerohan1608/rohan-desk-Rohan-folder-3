class company:
    def __init__(self):
        self.com_name = "TCS"
class developer(company):
    def __init__(self):
        self.dev_req = 10
        super().__init__()

class tester(company):
    def __init__(self):
        self.test_req = 8
        super().__init__()

class project(developer,tester):
    def __init__(self):
        self.pro_name = "Automation Anywhere"
        developer.__init__(self)
        tester.__init__(self)

def main():

    obj = project()
    print("Company names : ",obj.com_name)
    print("Project name is : ",obj.pro_name)
    print("Developers required : ",obj.dev_req)
    print("Testers required : ",obj.test_req)
    

main()
    
