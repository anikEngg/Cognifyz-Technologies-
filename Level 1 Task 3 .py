#!/usr/bin/env python
# coding: utf-8

# In[7]:


## Importing Libraries
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from scipy.stats import pearsonr
import plotly.express as px


# In[3]:


pip install geopandas


# In[4]:


pip install fiona shapely pyproj rtree


# In[6]:


pip install folium


# In[9]:


## Loading the Dataset
data = pd.read_csv('E:\Internship Task\Data Science Internship\Dataset.csv')


# In[10]:


## Visualizing the Locations of Restaurants on a Map
# Create a map of the world using Folium
world_map = folium.Map(location=[0, 0], zoom_start=2)


# In[11]:


# Add restaurant locations to the map
for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(world_map)


# In[12]:


# Save map to HTML file and display it
world_map.save("restaurant_locations.html")


# In[13]:


##Distribution of Restaurants Across Top 10 Cities
# Create a subset of the data containing only the top 10 cities
top_10_cities = data['City'].value_counts().nlargest(10).index
data_top_10_cities = data[data['City'].isin(top_10_cities)]


# In[15]:


# Create count plot for top 10 cities (horizontal bar plot)
plt.figure(figsize=(10, 6))
sns.countplot(data=data_top_10_cities, y='City', order=top_10_cities, palette='viridis')
plt.title("Distribution of Restaurants Across Cities")
plt.xlabel("Number of Restaurants")
plt.ylabel("Name of Cities")
plt.show()


# In[17]:


## Correlation Between Restaurant's Location and Its Rating:
# Calculate the correlation matrix
correlation_matrix = data[['Latitude', 'Longitude', 'Aggregate rating']].corr()


# In[18]:


# Create a heatmap to visualize the correlation
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Between Restaurant's Location and Rating")
plt.show()


# In[ ]:




