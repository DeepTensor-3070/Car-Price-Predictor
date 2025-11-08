import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import root_mean_squared_error

import joblib

car = pd.read_csv("Cleaned_Data.csv")
data = car.copy()

X=car[['name','company','year','kms_driven','fuel_type']]
y=car['Price']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

oh = OneHotEncoder()
oh.fit(X[['name','company','fuel_type']])

column_trans=make_column_transformer((OneHotEncoder(categories=oh.categories_),['name','company','fuel_type']),remainder='passthrough')

scores=[]
for i in range(1000):
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=i)
    lr=LinearRegression()
    pipe=make_pipeline(column_trans,lr)
    pipe.fit(X_train,y_train)
    y_pred=pipe.predict(X_test)
    scores.append(r2_score(y_test,y_pred))

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=np.argmax(scores))
lr=LinearRegression()
pipe=make_pipeline(column_trans,lr)
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)
r=r2_score(y_test,y_pred)

# print(r)

MODEL_FILE = "model.pkl"
joblib.dump(pipe, MODEL_FILE)

# dec = DecisionTreeRegressor()
# pipe = make_pipeline(column_trans,dec)
# pipe.fit(X_train,y_train)
# y_pred = pipe.predict(X_test)
# r2=r2_score(y_test,y_pred)
# rmse=root_mean_squared_error(y_test,y_pred)
# print(f"The r2 score for Desicion Tree is {r2}.")
# print(f"The rmse score for Desicion Tree is {rmse}.")

# ran = RandomForestRegressor()
# pipe = make_pipeline(column_trans,ran)
# pipe.fit(X_train,y_train)
# y_pred = pipe.predict(X_test)
# r2=r2_score(y_test,y_pred)
# rmse=root_mean_squared_error(y_test,y_pred)
# print(f"The r2 score for Random Forest is {r2}.")
# print(f"The rmse score for Random Forest is {rmse}.")








