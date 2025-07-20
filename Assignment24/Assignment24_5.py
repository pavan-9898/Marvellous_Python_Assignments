import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
     
    df=pd.DataFrame(data)

    
    df['Total']=df[['Math','Science','English']].sum(axis=1) 

    df['Status']=np.where(df['Total']>=250 ,"Pass","Fail")

    print(df)

    

if __name__=="__main__":
    main()