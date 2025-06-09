import time
import datetime
import schedule
import shutil

def backup():

    source="data.txt"
    destination="destination.txt"

    data=shutil.copyfile(source,destination)
    backup=open("backup.txt","a")
    backup.write("\n")
    backup.write(str(datetime.datetime.now()))
    print("data copied successfully")

def main():

   schedule.every(10).hour.do(backup)

   while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ =="__main__":
    main() 