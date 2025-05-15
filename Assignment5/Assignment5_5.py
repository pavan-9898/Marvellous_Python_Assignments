def even_odd(num):
    if num%2==0:
        print(F"{num}  is Even")
    else:
        print(f"{num} is Odd")
def main():
    print("Enter Number :")
    no=int(input())
    even_odd(no)
if __name__ == "__main__":
    main()