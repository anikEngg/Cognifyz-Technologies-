#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


## Loading the Dataset
data = pd.read_csv('E:\Internship Task\Data Science Internship\Dataset.csv')


# In[3]:


## Basic Statistical Measures for Numerical Columns
# Select Numerical Columns
numeric_columns = data.select_dtypes(include=[np.number])


# In[4]:


# Calculate basic statistical measures using describe()
summary_stats = numeric_columns.describe()
print(summary_stats)


# In[5]:


# Calculate standard deviation for numerical columns
sds = numeric_columns.std()
print("Standard deviation for numerical columns:")
print(sds)


# In[7]:


## Distribution of Categorical Variables
# Create count plot for Country Code
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Country Code', palette='viridis')
plt.title("Distribution of Restaurants by Country Codes")
plt.xlabel("Country Codes")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.show()


# In[14]:


## Top 10 Cities:
# Create a subset of the data containing only the top 10 cities
top_10_cities = data['City'].value_counts().nlargest(10).index
data_top_10_cities = data[data['City'].isin(top_10_cities)]


# In[15]:


# Create count plot for top 10 cities (horizontal bar plot)
plt.figure(figsize=(10, 6))
sns.countplot(data=data_top_10_cities, y='City', order=top_10_cities, palette='viridis')
plt.title("Top 10 Cities with Highest Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("Name of Cities")
plt.show()


# In[10]:


## Top Cuisines and Cities with the Highest Number of Restaurants
# Identify the top 10 cuisines and their counts
top_cuisines = data['Cuisines'].value_counts().nlargest(10)
top_cuisines_df = pd.DataFrame({'Cuisine': top_cuisines.index, 'Count': top_cuisines.values})

print("Top 10 Cuisines with the Highest Number of Restaurants:")
print(top_cuisines_df)


# In[13]:


# Identify the top 10 cities and their counts
top_city = data['City'].value_counts().nlargest(10)
top_city_df = pd.DataFrame({'City': top_city.index, 'Count': top_city.values})

print("Top 10 Cities with the Highest Number of Restaurants:")
print(top_city_df)

