#!/usr/bin/env python
# coding: utf-8

# ### Data Exploration and Preprocessing

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[4]:


# Load Dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[5]:


# View top 10 rows of the dataset
print(data.head(10))


# In[6]:


# Checking the Number of Rows and Columns
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])


# In[7]:


# Dataset Duplicate Value Count
dup = data.duplicated().sum()
print("Number of duplicate rows:", dup)


# In[8]:


# Check for missing values in each column and handle them accordingly

# Check for missing values
missing_values = data.isna().sum()
print("Missing values count per column:")
print(missing_values)


# In[9]:


# Check for empty values
empty_values = (data == "").sum()
print("Empty values count per column:")
print(empty_values)


# In[11]:


# Removing Rows with Empty Values in the "Cuisines" Column:
data = data[data['Cuisines'] != ""]


# In[12]:


# Check for empty values after removing
empty_values_after_removal = (data == "").sum().sum()
print("Empty values count after removal:", empty_values_after_removal)


# In[13]:


## Displaying Basic Information about the Dataset:
print(data.info())


# In[14]:


## Analyzing the Distribution of the Target Variable ("Aggregate rating")
target_counts = data['Aggregate rating'].value_counts()
print("Distribution of target variable:")
print(target_counts)


# In[15]:


# Visualize the distribution of the target variable
plt.figure(figsize=(10, 6))
sns.countplot(x='Aggregate rating', data=data, palette='viridis')
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Count')
plt.show()


# In[16]:


# Check if the distribution is balanced
is_balanced = np.all(target_counts >= target_counts.mean())
if is_balanced:
    print("The distribution of the target variable is balanced.")
else:
    print("The distribution of the target variable is imbalanced.")

