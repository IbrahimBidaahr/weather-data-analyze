#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python

# ## The Weather Dataset

# Here, the weather dataset is a time -series dataset with per-hour information about the weather condition in a particular location. it records temperature, dew point temperature, relative humidity,wind speed, velocity, pressure, and conditions.
# This data is available as a CSV file. We are going to analyses the dataset using pandas Dataframe.

# In[4]:


import pandas as pd


# In[8]:


data = pd.read_csv(r"C:\Users\surface\Data analyses project\file.csv")


# In[9]:


data


# ## How to Analyze DataFrames?

# ### .head()

# In[10]:


data.head()


# ### .shape

# In[11]:


data.shape


# ### .index

# In[13]:


data.index


# ### .columns

# In[14]:


data.columns


# In[15]:


# dtypes
data.dtypes


# In[17]:


# unique
data['Weather'].unique()


# In[18]:


# nonunique values
data.nunique()


# In[21]:


data.count()


# In[24]:


data['Weather'].value_counts()


# In[23]:


data.info()


# ### Q) 1.Find all the Unique "Wind speed" values in the datas.

# In[25]:


data.head(2)


# In[29]:


data.nunique()


# In[32]:


data['Wind Speed_km/h'].unique()


# In[33]:


data['Wind Speed_km/h'].nunique()


# ### Q2 Find the number of times when the "Weather is exactly Clear".

# In[34]:


data.head(2)


# In[35]:


data['Weather'].value_counts()


# In[40]:


data.head(2)
data[data.Weather=="Clear"]


# In[42]:


# groupby()
data.groupby('Weather').get_group('Clear')


# ### Q) 3. Find the number of times when the "Wind Speed was exactly 4km/h"

# In[44]:


data.head(2)


# In[45]:


data['Wind Speed_km/h'].value_counts()


# In[46]:


data[data['Wind Speed_km/h']==4]


# In[ ]:





# ### Q) 4. Find out all the Null values in the data

# In[49]:


data.isnull().sum()


# In[51]:


data.notnull().sum()


# ### Q) 5. Rename the column name "Weaher" of the dataframe to "Weather Condition"

# In[52]:


data.head(2)


# In[56]:


data.rename(columns ={'Weather': 'Weather Condition'}, inplace=True)


# In[57]:


data.head(2)


# ### Q) 6 What is the Mean "visibility"?

# In[58]:


data.head(2)


# In[59]:


data['Visibility_km'].mean()


# ### Q) 7 What is the Standard Deviation of Pressure in this data?

# In[60]:


data.head(2)


# In[61]:


data['Press_kPa'].std()


# ### Q) 8 What is the Variance of Relative humidity in this data?

# In[62]:


data.head(2)


# In[63]:


data['Rel Hum_%'].var()


# ### Q) 9. Find the intances when 'Snow' was recorded?

# In[64]:


data.head(2)


# In[66]:


data['Weather Condition'].value_counts()


# In[67]:


data[data['Weather Condition']=='Snow']


# In[68]:


data[data['Weather Condition'].str.contains('Snow')]


# ### Q) 10. find all instances when Wind speed is above 24 and visibilty is 25?

# In[69]:


data.head(2)


# In[71]:


data[(data['Wind Speed_km/h']> 24) & (data['Visibility_km'] ==25)]


# ### Q) 11. What is the mean values of each column against each weather conditons?

# In[73]:


data.head(2)


# In[116]:


data['Date/Time'] = pd.to_datetime(data['Date/Time'])


# In[117]:


data.dtypes


# In[118]:


data.groupby('Weather Condition').mean()


# In[77]:


pd.


# ### Q) 12. What is the minimum & maximum values of each column against each weathr conditions?

# In[78]:


data.head(2)


# In[80]:


data.groupby('Weather Condition').min()


# In[81]:


data.groupby('Weather Condition').max()


# ### Q) 13 Show all the records where weather conditions is fog?

# In[86]:


data[data['Weather Condition']=='Fog']


# In[87]:


data[data['Weather Condition'].str.contains('Fog')]


# In[ ]:





# ### Q) 14. Find all instances when Weather is clear or visibility is above 40?

# In[107]:


data[(data['Weather Condition']=='Clear') |(data['Visibility_km']>40)]


# ### Q) 15. Find all instances when:
#   ### A. Weather is clear and relative humidity is greater than 50
#    ### or
#   ### B. visibility is above 40
#             
# 

# In[109]:


data.head(2)


# In[112]:


data[(data['Weather Condition']=='Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]


# In[ ]:




