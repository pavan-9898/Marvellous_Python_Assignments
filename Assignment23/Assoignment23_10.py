import pandas as pd
import numpy as np

def main():

    data2={'Name':['Amit','Sagar','Pooja'],
          'Math':[np.nan,90,78],
           'Science':[92,np.nan,80],
           'English':[75,85,82]}
    
    df=pd.DataFrame(data2)

    df=df.drop('English',axis=1)

    print(df)



if __name__=="__main__":
    main()
