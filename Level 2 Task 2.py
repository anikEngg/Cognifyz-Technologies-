#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Load Dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[4]:


# Determine the most common price range among all the restaurants
most_common_price_range = data['Price range'].mode()[0]
print(f"Most Common Price Range: {most_common_price_range}")


# In[5]:


# Group by 'Price.range' and calculate the average rating
avg_rating_by_price_range = data.groupby('Price range')['Aggregate rating'].mean().reset_index()
avg_rating_by_price_range.columns = ['Price range', 'Average rating']
print("Average rating for each price range:")
print(avg_rating_by_price_range.round(2))


# In[6]:


# Find the price range with the highest average rating
highest_avg_rating_index = avg_rating_by_price_range['Average rating'].idxmax()


# In[7]:


# Create a bar plot
plt.figure(figsize=(10, 6))
colors = ['red' if i == highest_avg_rating_index else 'blue' for i in range(len(avg_rating_by_price_range))]
plt.bar(avg_rating_by_price_range['Price range'], avg_rating_by_price_range['Average rating'], color=colors)
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.title('Average Rating by Price Range')
plt.show()

