def temprature(cls):
    F=(cls*9/5)+32
    print(f"Temprature in Fahrenhit ",F)
def main():
    print("Enter Temprature In Celcius :")
    temp=int(input())
    temprature(temp)

if __name__== "__main__":
    main()