#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


# Load your dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[5]:


# Assuming the dataset is loaded into a dataframe called 'data'

# Create a histogram of ratings
plt.figure(figsize=(10, 6))
sns.histplot(data['Aggregate rating'], bins=np.arange(0, 5.3, 0.3), kde=False, color="skyblue", edgecolor="black")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Distribution of Ratings using Histogram")
plt.show()


# In[6]:


# Create a density plot of ratings
plt.figure(figsize=(10, 6))
sns.kdeplot(data['Aggregate rating'], shade=True, color="skyblue")
plt.xlabel("Rating")
plt.ylabel("Density")
plt.title("Distribution of Ratings using Density Plot")
plt.show()


# In[7]:


# Compare the average ratings of different cuisines
average_ratings_cuisine = data.groupby('Cuisines')['Aggregate rating'].mean().reset_index().sort_values(by='Aggregate rating', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='Aggregate rating', y='Cuisines', data=average_ratings_cuisine, palette='Blues_d')
plt.xlabel("Average Rating")
plt.ylabel("Cuisine")
plt.title("Average Ratings by Cuisines (Top 10)")
plt.show()


# In[8]:


# Compare the average ratings of different cities
average_ratings_city = data.groupby('City')['Aggregate rating'].mean().reset_index().sort_values(by='Aggregate rating', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Aggregate rating', y='City', data=average_ratings_city, palette='Blues_d')
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.title("Average Ratings by City (Top 10)")
plt.xticks(rotation=45)
plt.show()


# In[23]:


# Calculate the correlation matrix
correlation_matrix = data[["Aggregate rating", "Average Cost for two", "Votes", "Price range", "Has Table booking", "Has Online delivery"]].corr()

# Convert correlation matrix to DataFrame
correlation_df = correlation_matrix.stack().reset_index()
correlation_df.columns = ["Var1", "Var2", "Correlation"]


# In[28]:


# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()

