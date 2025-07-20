import numpy as np
import pandas as pd

def main():

    data={'Name':['A','B','C'],'Age':[21.0,22.0,23.0]}

    df=pd.DataFrame(data)

    print(df.dtypes)  # printing datatype

    df['Age']=df['Age'].astype(int) # converting age(float) to int 
    print(df)


if __name__=="__main__":
    main()