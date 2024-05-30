#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


##  Load the Dataset
# Load Dataset
data = pd.read_csv("E:\Internship Task\Data Science Internship\Dataset.csv")


# In[3]:


# View top 10 rows of the dataset
print(data.head(10))


# In[4]:


## Calculate Percentage of Restaurants Offering Table Booking and Online Delivery

# Total number of restaurants
total_num_restaurants = len(data)


# In[6]:


# Percentage calculation
table_booking_percentage = (data['Has Table booking'] == 'Yes').sum() / total_num_restaurants * 100
online_delivery_percentage = (data['Has Online delivery'] == 'Yes').sum() / total_num_restaurants * 100


# In[7]:


# Display results
print(f"Percentage of restaurants that offer Table Booking: {table_booking_percentage:.2f}%")
print(f"Percentage of restaurants that offer Online Delivery: {online_delivery_percentage:.2f}%")


# In[9]:


## Compare Average Ratings of Restaurants with and without Table Booking

# Average rating calculation
avg_rating_with_table = data[data['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
avg_rating_without_table = data[data['Has Table booking'] == 'No']['Aggregate rating'].mean()


# In[10]:


# Display results
print(f"Average rating with Table Booking: {avg_rating_with_table:.2f}")
print(f"Average rating without Table Booking: {avg_rating_without_table:.2f}")


# In[11]:


## Analyze Online Delivery Availability by Price Range
# Define price ranges
data['price_ranges'] = pd.cut(data['Average Cost for two'],
                              bins=[0, 500, 1000, float('inf')],
                              labels=['Low', 'Medium', 'High'])


# In[13]:


# Group by price range and online delivery availability
online_delivery_by_price_range = pd.crosstab(data['price_ranges'], data['Has Online delivery'], normalize='index')


# In[14]:


# Display results
print("Online Delivery Availability by Price Range:")
print(online_delivery_by_price_range)


# In[15]:


## Visualize Online Delivery Availability by Price Range
# Create a bar plot
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='price_ranges', hue='Has Online delivery')
plt.title('Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.show()

