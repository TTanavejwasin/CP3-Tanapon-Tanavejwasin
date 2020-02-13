class Vehicle:
    def openAircondition(self):
        print("Turn On : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Car")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car = Car()
car.openAircondition()
pickUp = PickUp()
pickUp.openAircondition()
van = Van()
van.openAircondition()
estateCar = Estatecar()
estateCar.openAircondition()

if __name__ == '__main__':

