#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score


# In[2]:


# Load Dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[3]:


# Create new numerical columns
data['Has Table booking_Num'] = np.where(data['Has Table booking'] == "Yes", 1, 0)
data['Has Online delivery_Num'] = np.where(data['Has Online delivery'] == "Yes", 1, 0)


# In[4]:


# Define predictor variables and target variable
predictors = ["Average Cost for two", "Votes", "Price range", "Has Table booking_Num", "Has Online delivery_Num"]
target_variable = "Aggregate rating"


# In[5]:


# Split data into training and testing sets
data_train, data_test = train_test_split(data, test_size=0.2, random_state=123)


# In[ ]:


# Train models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor(),
    "Support Vector Machine": SVR(kernel='linear')
}

results = {}

for name, model in models.items():
    scores = cross_val_score(model, data_train[predictors], data_train[target_variable], cv=5, scoring='neg_mean_squared_error')
    model.fit(data_train[predictors], data_train[target_variable])
    predictions = model.predict(data_test[predictors])
    rmse = np.sqrt(mean_squared_error(data_test[target_variable], predictions))
    r2 = r2_score(data_test[target_variable], predictions)
    results[name] = {"RMSE": rmse, "R-squared": r2}


# In[ ]:


# Print results
for name, result in results.items():
    print(name + " RMSE:", result["RMSE"])
    print(name + " R-squared:", result["R-squared"])
    print()

