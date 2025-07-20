import pandas as pd
from sklearn import preprocessing

def main():

    data={'City':['Pune','Mumbai','Delhi','Pune','Delhi']}

    df=pd.DataFrame(data)

    print(df)

    
    label_encoder = preprocessing.LabelEncoder()
    df['City']= label_encoder.fit_transform(df['City'])

    df['City'].unique()

    print(df)




if __name__=="__main__":
    main()