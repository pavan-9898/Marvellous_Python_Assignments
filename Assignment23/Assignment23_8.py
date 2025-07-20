import pandas as pd 
import matplotlib.pyplot as plt
def main():

    data={'Name':['Amit','Sagar','Pooja'],
          'Math':[85,90,78],
           'Science':[92,88,80],
           'English':[75,85,82]}

    df=pd.DataFrame(data)

    df['Total']=df[['Math','Science','English']].sum(axis=1) # here axis=1 bcz it add row wise
    print(df)

    x=df['Total']
    y=df['Name']

    plt.plot(x,y,marker='o',linestyle='-')
    plt.show()

    

   



if __name__=="__main__":
    main()