def voting(age):
    if age>=18:
        print("Eligible to vote ")
    else:
        print("Not Eligible ")

def main():
    print("Enter Age :")
    age=int(input())
    voting(age)
if __name__ == "__main__":
    main()