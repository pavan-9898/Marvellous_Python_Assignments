import multiprocessing

def square_list(my_list):
    for i in my_list:
        print(i*i)

def main():

    p1=multiprocessing.Process(target=square_list,args=([10,20,30,40,50],))
    p1.start()
    p1.join()

    print("------------- P1 Complted--------")

    p2=multiprocessing.Process(target=square_list,args=([60,70,80,90,100],))
    p2.start()
    p2.join()

    print("-------------- P2 Completed ------")

if __name__ == "__main__":
    main()