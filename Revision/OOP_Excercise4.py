class Demo:

    def __init__(self):
        self.i=0
        self.j=0

    def fun(self):
        print("Inside Instance method")

    @classmethod
    def gun(cls):
        print("Inside Class Method")
    
    @staticmethod
    def sun():
        print("Inside Static Method")

def main():

    obj=Demo()
    obj.fun()
    obj.gun()
    obj.sun()


if __name__ == "__main__":
    main()