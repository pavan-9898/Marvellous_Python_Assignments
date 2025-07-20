import pandas as pd


def main():

    data={'Garde':['A+','B','A','C','B+']}

    df=pd.DataFrame(data)

    print("Before Replace")

    print(df)

    print("**********************")

    df=df.replace({'A+':'Excellent','A':'very good','B':'Average','C':'Poor','B+':'Good'})

    print("After Replace")

    print(df)

    print("******************************")





if __name__=="__main__":
    main()