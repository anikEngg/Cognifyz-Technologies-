#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Load Dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[4]:


# Extract additional features

# Create a new column for the length of restaurant names
data['Restaurant Name Length'] = data['Restaurant Name'].apply(len)


# In[5]:


# Create a new column for the length of restaurant addresses
data['Address Length'] = data['Address'].apply(len)


# In[6]:


# Display the updated DataFrame
print(data.head())


# In[7]:


# Encode categorical variables

# Create new columns for Has Table Booking and Has Online Delivery
data['Has Table Booking'] = data['Has Table booking'].apply(lambda x: 1 if x == "Yes" else 0)
data['Has Online Delivery'] = data['Has Online delivery'].apply(lambda x: 1 if x == "Yes" else 0)


# In[8]:


# Display the updated DataFrame
print(data.head())


# In[ ]:




