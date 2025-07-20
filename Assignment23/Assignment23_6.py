import pandas as pd

def main():

    Line="*"*50

    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
    
    df=pd.DataFrame(data)

    print("Before Sorting")

    df['Total']=df[['Math','Science','English']].sum(axis=1) # here axis=1 bcz it add row wise
    print(df)

    print(Line)

    print("After Sorting")

    print(df.sort_values(by=['Total'],ascending=False))

    print(Line)


if __name__=="__main__":
    main()