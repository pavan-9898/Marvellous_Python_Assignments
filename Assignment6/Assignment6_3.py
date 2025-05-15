def table(no):
    mul=1
    for i in range(1,11):
        
        print(f"{no} * {i} ={i*no}")

def main():
    print("enter a number")
    no=int(input())
    # mul=1
    # for i in range(1,11):
        
    #     print(f"{no} * {i} ={i*no}")
    table(no)
        
if __name__ == "__main__":
    main()