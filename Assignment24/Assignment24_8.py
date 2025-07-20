import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
     
    df=pd.DataFrame(data)

    df['Gender']=['Male','Male','Female']

    df['Total']=df[['Math','Science','English']].sum(axis=1) 

    df['Status']=np.where(df['Total']>=250 ,"Pass","Fail")

    plt.hist(df['Math'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Histogram of Math")
    plt.show()


if __name__=="__main__":
    main()