def palindrome(name):
    if name==name[::-1]:
        print("String is palindrome ")
    else:
        print("String is not palindrome")

def main():
    print("Enter String :")
    name=input()
    # print(name[::-1])
    palindrome(name)
    
    # if name==name[::-1]:
    #     print("String is palindrome ")
    # else:
    #     print("String is not palindrome")

if __name__ == "__main__":
    main()