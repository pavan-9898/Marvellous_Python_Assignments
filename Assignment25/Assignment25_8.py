import pandas as pd
import numpy as np

def main():

    data={'Marks':[85,np.nan,90,np.nan,95]}

    s=pd.Series(data)

    print(s)


    new_s=s.interpolate(method='polynomial', order=2)
    print(new_s)

if __name__=="__main__":
    main()