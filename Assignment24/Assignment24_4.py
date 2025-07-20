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

     print(df)

     marks=df['Math'][1],df['Science'][1],df['English'][1]
     labels=['Math','Science','English']

     plt.pie(marks,labels=labels,autopct='%1.1f%%') 
     plt.title("Sagar's Subject Marks Pie Chart")
     plt.show()

     

     print(df)

if __name__=="__main__":
     main()