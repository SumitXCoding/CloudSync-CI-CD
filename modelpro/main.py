import numpy as np
import pandas as pd

df = pd.read_csv("insurance.csv")

# print(df.head())

# print(df.isnull().sum())


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['sex'] = le.fit_transform(df['sex'])
df['smoker'] = le.fit_transform(df['smoker'])
df['region'] = le.fit_transform(df['region'])

# print(df.head())

x = df.drop(columns='charges')
y = df['charges']
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

from sklearn.metrics import r2_score

print(r2_score(y_test,y_pred))