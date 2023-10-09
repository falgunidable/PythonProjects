class Vehicle:
    def __init__(self,make,model):      # self - object that is created -   the ones written inside are properties
        self.make = make        # we are referring object to itself  
        self.model = model
    def get_model_make(self):
        print(f"I'm a {self.make} {self.model}")
    def moves(self):
        print("Moving..")

myCar = Vehicle('Tesla','Model 3')
# print(myCar.model)
# print(myCar.make)
myCar.get_model_make()
myCar.moves()

myCar = Vehicle('Valorine','Model 3')
# print(myCar.model)
# print(myCar.make)
myCar.get_model_make()
myCar.moves()

#   Inheritance
class Aeroplane(Vehicle):
    #   if I want to add an extra attribute to the aeroplane class we need to have the init method again
    #   so we are going to override it from parent class
    def __init__(self,make,model,a_id):
        super().__init__(make,model)    #   taking the same values from the parent class
        self.a_id = a_id
    def get_model_make(self):
        print(f"I'm a {self.make} {self.model} with id {self.a_id}")
    #   overriding the parent function
    def moves(self):
        print("Flying..")

class Truck(Vehicle):
    #   overriding the parent function
    def moves(self):
        print("Rumbling..")

class GolfCart(Vehicle):
    pass    # inherit as it is, not overriding the moves method

plane = Aeroplane('Spicejet','Model 2',12345)
truck = Truck('Tussy','Pinnacle')
golf = GolfCart('Golfy','231G3')

plane.get_model_make()
plane.moves()
truck.get_model_make()
truck.moves()
golf.get_model_make()
golf.moves()

print("\n\n")

#   Polymorphisim - ability to do tasks in multiple ways
for v in (myCar , plane, truck, golf):
    v.get_model_make()
    v.moves()