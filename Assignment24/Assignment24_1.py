import pandas as pd
import numpy as np

def main():

     data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
     
     df=pd.DataFrame(data)

     print(df)

     min_val=df['Math'].min()
     max_val=df['Math'].max()

    #  print(min_val)
    #  print(max_val)

     math_normalize = (df['Math'] - min_val) / (max_val - min_val)
     print(math_normalize)





if __name__=="__main__":
    main()