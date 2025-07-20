import pandas as pd

def main():
   
    Line="*"*50
    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
    
    df=pd.DataFrame(data) # converting dictionary to dataframe 
    print(Line)
    print("Shape of datframe ")
    print(df.shape) # printing shape of dataframe
    print(Line)

    print("Statastical information of dataframe is :")
    print(df.describe()) # statastical informataion
    print(Line)

    print("Columns of the dataframe is :")
    print(df.columns) # prints the columns of dataframe 
    print(Line)

    print("Data Types :")
    print(df.dtypes)
    print(Line)


if __name__=="__main__":
    main()