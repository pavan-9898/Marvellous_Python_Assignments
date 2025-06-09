import time
import datetime
import schedule


def Write_Current_Time_In_File():

    fobj=open("Marvellous.txt","a")  # this will create new file if not exists 
                                     #if it is exist already then it will open in append mode
    fobj.write(str(datetime.datetime.now()))
    fobj.write("\n")
    fobj.close()
    print("Time has been written in the file")

def main():

    schedule.every(5).minutes.do(Write_Current_Time_In_File)


    while True:
        schedule.run_pending()
        time.sleep(1)
    




if __name__ =="__main__":
    main() 