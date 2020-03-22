#!/usr/bin/env python
# coding: utf-8

# Assignment 3

# In[43]:


import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


# Load Dataset

# In[70]:


data = pd.read_csv("listings.csv", delimiter=",")
print(data.dtypes)
print(data.isna().values.any())
data = data.dropna()
print(data.isna().values.any())


# Change some types to countable type

# In[76]:


myset = set(data["room_type"])
print(myset)

myset2 = set(data["neighbourhood_group"])
print(myset2)

myset3 = set(data["neighbourhood"])
print(myset3)

data["room_type"] = pd.Categorical(data["room_type"])
data["room_type"] = data["room_type"].cat.rename_categories([1,2,3])
data["room_type"] = data["room_type"].cat.codes
data["room_type"] = data["room_type"]+1
print(data["room_type"])

data["neighbourhood_group"] = pd.Categorical(data["neighbourhood_group"])
data["neighbourhood_group"] = data["neighbourhood_group"].cat.rename_categories([1,2,3,4,5])
data["neighbourhood_group"] = data["neighbourhood_group"].cat.codes
data["neighbourhood_group"] = data["neighbourhood_group"]+1
print(data["neighbourhood_group"])


# Mean and Variance of each Continuous Random Variables

# In[15]:


print("Latitude Mean: ",data["latitude"].mean())
print("Latitude Variance: ",data["latitude"].var())

print("Longitude Mean: ",data["longitude"].mean())
print("Longitude Variance: ",data["longitude"].var())

print("Reviews per month Mean: ",data["reviews_per_month"].mean())
print("Reviews per month Variance: ",data["reviews_per_month"].var())


# Mean and Variance of each Discrete Random Variables * countable only

# In[78]:


print("Id Mean : ",data["id"].mean())
print("Id Var : ",data["id"].var())

print("Host Id Mean : ",data["host_id"].mean())
print("Host Id Var : ",data["host_id"].var())

print("Price Mean : ",data["price"].mean())
print("Price Var : ",data["price"].var())

print("Minimum Night Mean : ",data["minimum_nights"].mean())
print("Minimum Night Var : ",data["minimum_nights"].var())

print("Number of Reviews Mean : ",data["number_of_reviews"].mean())
print("Number of Reviews Var : ",data["number_of_reviews"].var())

print("availability 365 Mean : ",data["availability_365"].mean())
print("availability 365 Var : ",data["availability_365"].var())

print("Room Type Mean : ",data["room_type"].mean())
print("Room Type Var : ",data["room_type"].var())

print("Neighbourhood Group Mean : ",data["neighbourhood_group"].mean())
print("Neighbourhood Group Var : ",data["neighbourhood_group"].var())

print("Calculated Host Listings count Mean : ",data["calculated_host_listings_count"].mean())
print("Calculated Host Listings count Var : ",data["calculated_host_listings_count"].var())


# In[ ]:




