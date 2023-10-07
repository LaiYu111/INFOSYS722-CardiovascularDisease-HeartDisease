import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import os
import matplotlib.pyplot as plt

def bar_plot(variables=None, data=None, title="Cardiovascular Disease", xlabel="value", ylabel="Categories"):
    x = np.arange(len(variables))
    width = 0.35

    bars = plt.bar(x, data, width)


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


    plt.legend()

    plt.xticks(x, variables)
    plt.xticks(rotation=30)

    for bar, proportion in zip(bars, data):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{(proportion * 100):.1f}%', ha='center', va='bottom')


    plt.show()
    

def generate_CVD_dataset():
    if os.path.exists('./Database/CardiovascularDisease/CVD_unclean.csv'):
        print("CVD_uncleaned.csv existed.")
    else:
        cvd_cleaned_data_df = pd.read_csv('./Database/CardiovascularDisease/CVD_cleaned.csv')
        error_data = {}
        missing_value = np.nan
        row = cvd_cleaned_data_df.shape[0]
        column = cvd_cleaned_data_df.shape[1]

        # there are 308854 * 19 data and each data 1/10000 * 1/6 chance that it will become a missing value.
        for r in range(row):
            num = random.randint(1, 10000)  # 1/10000 chance to select a target row
            if num == 1:
                for key, value in error_data.items():
                    if random.randint(1, 6) == 1:  # 1/6 chance to add a missing value to a target cell
                        cvd_cleaned_data_df.loc[r, key] = missing_value

        cvd_cleaned_data_df.to_csv("./Database/CardiovascularDisease/CVD_unclean.csv", index=False)
        print("finished")
        
        
def bmi_2_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Normal'
    elif 25 <= bmi <= 29.9:
        return 'Overweight'
    else:
        return 'Obese'
    
def alcohol_consumption_2_category(alcohol):
    if alcohol == 0:
        return 'Zero Alcohol Consumption'
    elif alcohol <= 7.5:
        return 'Low Alcohol Consumption'
    elif 7.5 < alcohol <= 15:
        return 'Medium Alcohol Consumption'
    elif 15 < alcohol <= 22.5:
        return 'High Alcohol Consumption'
    else:
        return "Excess Alcohol Consumption"
    
def fruit_consumption_2_category(fruit):
    if fruit == 0:
        return 'Zero Fruit Consumption'
    elif fruit <= 30:
        return 'Low Fruit Consumption'
    elif 30 < fruit <= 60:
        return 'Medium Fruit Consumption'
    elif 60 < fruit <= 90:
        return 'High Fruit Consumption'
    else:
        return "Excess Fruit Consumption"
    
def friedpotato_consumption_2_category(friedpotato):
    if friedpotato == 0:
        return 'Zero friedpotato Consumption'
    elif friedpotato <= 30:
        return 'Low friedpotato Consumption'
    elif 30 < friedpotato <= 60:
        return 'Medium friedpotato Consumption'
    elif 60 < friedpotato <= 90:
        return 'friedpotato friedpotato Consumption'
    else:
        return "Excess friedpotato Consumption"
    
def greenvega_consumption_2_category(greenvega):
    if greenvega == 0:
        return 'Zero greenvega Consumption'
    elif greenvega <= 30:
        return 'Low greenvega Consumption'
    elif 30 < greenvega <= 60:
        return 'Medium greenvega Consumption'
    elif 60 < greenvega <= 90:
        return 'friedpotato greenvega Consumption'
    else:
        return "Excess greenvega Consumption"
    
def convert_XPT():
    if os.path.exists('./Database/CardiovascularDisease/CVD_unclean_2021.csv'):
        print("CVD_unclean_2021.csv existed.")
    else:
        xpt_file_path = './Database/CardiovascularDisease/LLCP2021.XPT'  
        data = pd.read_sas(xpt_file_path, format='xport')  
    	# Convert to a .csv file  
        csv_file_path = './Database/CardiovascularDisease/CVD_unclean_2021.csv'  
        data.to_csv(csv_file_path, index=False)
        print("Finished")

def generate_current_CVD_dataset(file_path, DataFrame):
    if os.path.exists(file_path):
        print(f"{file_path} File existed.")
    else:
        DataFrame.to_csv(file_path, index=False)
        print("Finished")
        
        
