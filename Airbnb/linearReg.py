# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# load data
data = pd.read_csv('../data/AB_NYC_2019.csv')
print(data.head(10))

# data preparation
print(data.isnull().sum())
data.drop(['id', 'name', 'host_id', 'host_name', 'last_review'], axis=1, inplace=True)
print(print(data.isnull().sum()))
data.fillna({'reviews_per_month': 0}, inplace=True)
print(print(data.isnull().sum()))
Min_Price = min(data['price'].value_counts())
Max_Price = max(data['price'].value_counts())
Mean_Price = data['price'].value_counts().mean()

# if Mean_Price*2 < data['price'] & data['price'] < Mean_Price*4:
#     data['Category'] = 'Expensive'
# elif data['price'] >= Mean_Price*4:
#     data['Category'] = 'Super Expensive'
# elif Mean_Price < data['price'] & data['price'] <= Mean_Price*2:
#     data['Category'] = 'Medium'
# elif Mean_Price*(3/4) < data['price'] & data['price'] <=Mean_Price:
#     data['Category'] = 'Reasonable'
# elif Mean_Price/2 < data['price'] & data['price'] <= Mean_Price*(3/4):
#     data['Category'] = 'Cheap'
# elif data['price'] <= Mean_Price/2:
#     data['Category'] = 'Very Cheap'
#
# print(data['Category'].value_counts())

data['Category'] = data['price'].apply(lambda x: 'Super Expensive' if x > Mean_Price * 4
else ('Expensive' if Mean_Price * 2 <= x < Mean_Price * 4
      else ('Medium' if Mean_Price <= x < Mean_Price * 2
            else ('Reasonable' if Mean_Price * (3 / 4) <= x < Mean_Price
                  else ('Cheap' if Mean_Price / 2 <= x < Mean_Price * (3 / 4)
                        else 'very cheap')))))

print(data['Category'].value_counts())

data.drop(['neighbourhood', 'latitude', 'longitude', 'number_of_reviews', 'reviews_per_month'], axis=1,inplace=True)
print(data.isnull().sum())

def Encode(f):
    for column in data.columns[data.columns.isin(['neighbourhood_group', 'room_type', 'Category'])]:
        data[column] = data[column].factorize()[0]
    return data

new_data = Encode(data.copy())
print(new_data)
print(new_data.info())


