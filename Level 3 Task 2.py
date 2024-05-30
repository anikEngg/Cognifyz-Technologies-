#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load Dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[3]:


# View top 10 rows of the dataset
print(data.head(10))


# In[4]:


## Analyze the Relationship Between the Type of Cuisine and the Restaurant's Rating
## Identify the Top 10 Cuisines


# In[5]:


# Identify the top 10 cuisines
top_cuisines = data['Cuisines'].value_counts().head(10).index.tolist()


# In[6]:


# Subset the data for only the top 10 cuisines
data_top_cuisines = data[data['Cuisines'].isin(top_cuisines)]


# In[8]:


# Create a box plot to visualize the distribution of ratings for each cuisine type (top 10)
plt.figure(figsize=(12, 8))
sns.boxplot(x='Cuisines', y='Aggregate rating', data=data_top_cuisines)
plt.xticks(rotation=45)
plt.xlabel('Cuisine Type')
plt.ylabel('Rating')
plt.title('Distribution of Ratings by Cuisine Type')
plt.show()


# In[9]:


# Group the data by cuisine and calculate the total number of votes for each cuisine
popular_cuisines = data.groupby('Cuisines')['Votes'].sum().reset_index()


# In[10]:


# Sort the cuisines by total votes in descending order
popular_cuisines = popular_cuisines.sort_values(by='Votes', ascending=False)


# In[11]:


# Print the top 10 most popular cuisines
print(popular_cuisines.head(10))


# In[12]:


# Calculate the average rating for each cuisine
average_ratings = data.groupby('Cuisines')['Aggregate rating'].mean().reset_index()


# In[13]:


# Sort the cuisines by average rating in descending order
average_ratings = average_ratings.sort_values(by='Aggregate rating', ascending=False)


# In[14]:


# Print the cuisines with the highest average ratings
print(average_ratings.head(10))

