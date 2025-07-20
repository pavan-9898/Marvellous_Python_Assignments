import numpy as np
import pandas as pd

def main():

    data={'Salary':[25000,27000,29000,31000,50000,100000]}

    data=np.sort(data['Salary'])  # sorting data in ascending order

    # calculating Q1, Q2,Q3 and IQR

    Q1 = np.percentile(data, 25, interpolation = 'midpoint') 
    Q2 = np.percentile(data, 50, interpolation = 'midpoint') 
    Q3 = np.percentile(data, 75, interpolation = 'midpoint')

    print('Q1 25 percentile of the given data is, ', Q1)
    print('Q1 50 percentile of the given data is, ', Q2)
    print('Q1 75 percentile of the given data is, ', Q3)

    IQR=Q3-Q1

    print('Interquartile range is', IQR) 

    # Finding Lower And Upper Limits

    low_lim = Q1 - 1.5 * IQR
    up_lim = Q3 + 1.5 * IQR
    print('low_limit is', low_lim)
    print('up_limit is', up_lim)

    outlier =[]
    for x in data:
     if ((x> up_lim) or (x<low_lim)):
         outlier.append(x)
    print(' outlier in the dataset is', outlier)



    
  

if __name__=="__main__":
    main()