#private access modifier '_ _' to access this we use getter and settor methods

# Getter and Setter methods :

class car:
    def __init__(self):
        self.color = "Blue"
        self.seats = 4
        self.__engine = "Petrol"
        self.__trans = "Manual"
    def get_car_info(self):
        print("Car Information")
        print("The car is : ",self.color)
        print("It is having",self.seats,"seats.")
        print("Engine type is",self.__engine)
        print("Transmission is",self.__trans)
    def set_car_engine(self,engine,trans = "Automatic"):
        self.__engine = engine
        self.__trans = trans

obj = car()
obj.get_car_info()
obj.set_car_engine("Electric") 
obj.get_car_info()
