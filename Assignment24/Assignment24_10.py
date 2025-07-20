import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():

     data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],        
           'English':[75,85,82]}
     
     df=pd.DataFrame(data)

     df['Gender']=['Male','Male','Female']

     df['Total']=df[['Math','Science','English']].sum(axis=1) 

     df['Status']=np.where(df['Total']>=250 ,"Pass","Fail")

     df.rename(columns={'Math': 'Mathematics'}, inplace=True)

     plt.boxplot(df['English'])
     plt.show()


if __name__=="__main__":
    main()