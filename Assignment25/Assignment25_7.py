import pandas as pd
import numpy as np

def main():

    Line="*"*50

    data={'Age':[18,22,25,30,35]}

    df=pd.DataFrame(data)

    print(df)

    min_val=np.min(df)
    max_val=np.max(df)

    print(Line)

    print(min_val)
    print(max_val)

    print(Line)

    normalized_data = (df - min_val) / (max_val - min_val)

    print(normalized_data)


    
if __name__=="__main__":
    main()