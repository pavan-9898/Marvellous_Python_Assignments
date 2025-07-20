import pandas as pd

def main():

    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}
    
    df=pd.DataFrame(data)

    print(df.replace(to_replace=r'Pooja',value='Puja',regex=True))
    


if __name__=="__main__":
    main()