import psutil
import sys
import os
import time

def ProcessDirectory(DirName):

    if not os.path.exists(DirName):
        os.mkdir(DirName)
    
    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    timestamp=timestamp.replace("/","_")
  
    fname=os.path.join(DirName,"processlog%s.log" %(timestamp))
    
    fobj=open(fname,'w')

    Border="*"*70
    fobj.write(Border)
    fobj.write("\n\t\t This file contains information about the process\n")
    fobj.write(Border)
    
        
    for proc in psutil.process_iter():
        
        info=proc.as_dict(attrs=['name','pid','username'])
        
        fobj.write("\n"+str(info)+"\n")
    fobj.close()

def main():

    DirName=sys.argv[1]

    ProcessDirectory(DirName)

if __name__=="__main__":
    main()