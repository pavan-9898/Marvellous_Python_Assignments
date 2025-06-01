class Vehicle:

    def start(self):

        print("Starting the vehicle ..")

class Car(Vehicle):

    def start(self):

        print("Vehicle Started..")

def main():

    obj1=Vehicle()
    obj1.start()
    obj2=Car()
    obj2.start()


if __name__ == "__main__":
    main()