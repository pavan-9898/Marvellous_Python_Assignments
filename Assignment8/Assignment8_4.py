import threading

def upper(name):
    length=len(name)
    count=0
    for i in range(length) :
        if name[i].isupper():
            count=count+1
    
    print("Total Number of upper character is : ",count)

    print("ID and name of thread is : ",threading.get_ident(),threading.current_thread())
    print()
        
def lower(name):
    length=len(name)
    count=0
    for i in range(length):
        if name[i].islower():
            count=count+1
    print("Total Number of Lower caracter is :",count)

    print("ID and name of thread is : ",threading.get_ident(),threading.current_thread())
    print()


def digit(name):
    length=len(name)
    count=0

    for i in range(length):
        if name[i].isdigit():
            count=count+1
    print("Total Number of digit is :",count)

    print("ID and name of thread is : ",threading.get_ident(),threading.current_thread())
    print()


def main():

    # capital("paVaN")
    # small("pavanKumarSupekar")
    # digit("pavansup98ekar76r")
    
    given_string="pavanKumarSupekar1998"
    small=threading.Thread(target=lower,args=(given_string,))
    small.start()
    small.join()

    capital=threading.Thread(target=upper,args=(given_string,))

    capital.start()
    capital.join()

    digit1=threading.Thread(target=digit,args=(given_string,))

    digit1.start()
    digit1.join()

    # small.start()
    # capital.start()
    # digit1.start()

    # small.join()
    # capital.join()
    # digit1.join()

    

    print("Exit from main.")

    


if __name__ == "__main__":
    main()