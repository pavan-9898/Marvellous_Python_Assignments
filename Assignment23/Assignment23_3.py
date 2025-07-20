import pandas as pd 

def main():

    
    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
    
    df=pd.DataFrame(data) # converting  to dataframe 

    df['Total']=df[['Math','Science','English']].sum(axis=1) # here axis=1 bcz it add row wise
    print(df)





if __name__=="__main__":
    main()