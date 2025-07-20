import pandas as pd

def main():

    Line="*"*50
    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
    
    df=pd.DataFrame(data) # converting  to dataframe

    print(Line)
    print("Descriptive Statastics Of dataframe is :")
    print(df.describe())
    print(Line)





if __name__=="__main__":
    main()