import multiprocessing
import multiprocessing.pool

def factorial(no):
 if no==0:
    return 1
 else:
    return no*factorial(no-1)
    
    
    

def main():

    data=[5,4,3,2,1]
    # result=list()

    p1=multiprocessing.Pool()

    result=p1.map(factorial,data)
    print(result)

    p1.close()
    p1.join()
    

if __name__ == "__main__":
    main()