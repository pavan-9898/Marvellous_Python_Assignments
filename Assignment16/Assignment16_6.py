import shutil

def main():

 source="data.txt"
 destination=open("destination.txt","w")
 destination.close()
 destination="destination.txt"
 shutil.copyfile(source,destination)
 
 print(f"file content copied from  {source} to {destination} file successfully")




if __name__ =="__main__":
    main() 