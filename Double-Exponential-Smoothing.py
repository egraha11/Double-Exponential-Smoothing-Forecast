import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy



def double_exp_smooting(data):

    alpha = .5
    beta = .5

    arr = np.array([data.Year, data.Revenue])

    df = pd.DataFrame({"Level":[], 'Trend':[], 'Forecast':[], "Error":[]})

    first_row = {"Level": arr[1,0], "Trend":arr[1,1]- arr[1,0], 'Forecast':arr[1,0], "Error":0}

    df = df.append(first_row, ignore_index = True)

    df.at[1,"Forecast"]= arr[1,1]

    for i in range(1, len(arr[1])):

        
        level = (alpha*arr[1, i]) + ((1-alpha) * (df.iloc[i - 1, 0] + df.iloc[i - 1, 1]))
        df.at[i, "Level"] = level

        trend = beta*(df.iloc[i,0] - df.iloc[i - 1, 0]) + ((1-beta) * df.iloc[i - 1, 1])
        df.at[i, "Trend"] = trend

        forecast = level + trend
        df.at[i+1, "Forecast"] = forecast

        error = arr[1,i] - df.iloc[i, 2]
        df.at[i, "Error"] = error
        

    plt.plot(arr[0], arr[1], color="red", label="Actual")
    plt.plot(np.arange(2005, 2022, 1), df.Forecast, color="blue", label="Forecast")
    plt.title("Double Exponential Smoothing")
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Revenue")

    plt.show()


    print("Actual Revenue   Forecasted Revenue\n -----------------------")
    for i in range(len(arr[1])):
        print(str(arr[1, i]) + "                   " + str(int(df.iloc[i, 2])))

    print("Forecast Details\n--------------\n")
    print(df)


df = pd.DataFrame({"Year" : [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], 
"Revenue": [13931, 19315, 24578,37491, 42905, 65225, 108249, 156508, 170910, 182795, 233715, 215639, 229234, 265595, 260174, 274515]})



double_exp_smooting(df)