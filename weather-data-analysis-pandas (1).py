#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pandas')


# In[5]:


import pandas as pd


# In[6]:


data = pd.read_csv(r"C:\Users\asifs\Downloads\1. Weather Data.csv")
data


# In[7]:


data.head()


# In[8]:


data.shape


# In[9]:


data.index


# In[10]:


data.columns


# In[11]:


data.dtypes


# In[12]:


data['Weather'].unique()


# In[13]:


data.nunique()


# In[14]:


data.count()


# In[15]:


data["Weather"].value_counts()


# In[16]:


data.info()


# In[17]:


data.head(2)


# In[18]:


data.nunique()


# In[19]:


data["Wind Speed_km/h"].unique()


# In[20]:


#find the number of times when the weather is exactly clear
#There are three ways we can find this 1.by count funct         2. by filtering        3. by group by


# In[21]:


data.head(5)


# In[22]:


data.Weather.value_counts()


# In[23]:


#2 filtering
data.head()


# In[24]:


data[data.Weather == "Clear"]


# In[25]:


#3 groupby
data.groupby('Weather').get_group('Clear')


# In[26]:


#find when exactly how many times wind speed is 4km.h


# In[27]:


data[data['Wind Speed_km/h'] == 4]


# In[28]:


#finding all null values
data.isnull().sum()      #it will count the number of rows which are null


# In[29]:


data.notnull().sum()       #it will count the number of rows which arent blank or having values


# In[30]:


#rename data table
data.head(2)


# In[31]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# In[32]:


data.head(2)


# In[36]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace=True)
#to make it permenant change in the coumn name 
#u have to add inplace = true in cmnd


# In[37]:


data.head(2)


# In[38]:


#mean visibility


# In[39]:


data.head(2)


# In[40]:


data.Visibility_km.mean()


# In[42]:


#standard deviation of pressure 
data.Press_kPa.std()


# In[43]:


#variance relative humidity
data["Rel Hum_%"].var()


# In[44]:


#instances when snow is recorded
#value_counts
data['Weather Condition'].value_counts()


# In[46]:


#filtering
data[data['Weather Condition']=='Snow']


# In[48]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# In[49]:


#instances when wind speed is above 24 and visibility is 25


# In[50]:


data.head(2)


# In[52]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# In[53]:


#mean value of every column against weather condition


# In[54]:


data.groupby('Weather Condition').mean()


# In[55]:


#min and max value of each column against weather condition


# In[56]:


data.groupby('Weather Condition').min()


# In[57]:


data.groupby('Weather Condition').max()


# In[58]:


#all records where weather condition is fog


# In[61]:


data[data['Weather Condition'] == 'Fog']


# In[62]:


#find all instances where weather is clear or visibility is greather than 40


# In[63]:


data[(data['Weather Condition']=='Clear') | (data['Visibility_km']>40)]


# In[64]:


#weather is clear and humidity > 50
# OR visibility > 40


# In[67]:


data[(data['Weather Condition']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]


# In[ ]:




