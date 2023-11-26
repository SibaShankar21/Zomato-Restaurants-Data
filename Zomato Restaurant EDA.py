#!/usr/bin/env python
# coding: utf-8

# # zomato Restaurants EDA
#     Author: Siba Shankar Mahapatra

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


df=pd.read_csv(r"C:\Users\91832\Downloads\archive (1)\zomato.csv",encoding ='latin-1')


# In[8]:


df.head()


# In[11]:


df.columns


# In[12]:


df.isnull().sum()


# In[13]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[14]:


df_countries = pd.read_excel(r"C:\Users\91832\Downloads\archive (1)\Country-Code.xlsx")


# In[15]:


df_countries.head()


# In[16]:


df_countries.info()


# In[17]:


df_countries.describe()


# In[18]:


df.columns


# In[19]:


df_final = pd.merge(df,df_countries,on='Country Code',how='left')


# In[20]:


df_final.head()


# In[21]:


df_final.Country.value_counts().index


# In[22]:


country_names = df_final.Country.value_counts().index


# In[31]:


df_final.Country.value_counts().value_counts


# In[23]:


df_final.Country.value_counts().values


# In[24]:


country_val=df_final.Country.value_counts().values


# In[25]:


#plot a bar chart
plt.bar(country_names[:3],country_val[:3])
# Adding labels and title
plt.xlabel('country_names')
plt.ylabel('country_val')
plt.title('Country & zomato popularity')

# Display the plot
plt.show()


# In[26]:


plt.pie(country_val[:3],labels = country_names[:3],autopct='%1.2f%%')


# OBSERVATION :
# Zomato maxium sales in India and after that USA and then United Kingdom

# In[27]:


df_final.columns


# In[53]:


df_final.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size()


# In[28]:


#convert the above data into dataframe
df_final.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[29]:


ratings = df_final.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[60]:


ratings


# ### OBSERVATIONS
# RATING 4.5 - 4.9 --->EXCELLENT
# RATING 4.0 - 4.4 --->VERY GOOD
# RATING 3.5 - 3.9 --->GOOD
# RATING 2.5 - 3.4 --->AVERAGE
# RATING 1.8 - 2.4 --->POOR
# RATING 0.0 ---> NOT RATED

# In[64]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x='Aggregate rating',y='Rating count',data=ratings)


# In[68]:


sns.barplot(x='Aggregate rating',y='Rating count',hue ='Rating color', data=ratings, palette=['blue','red','orange','yellow','green','green'])


# In[71]:


### find the countries name that has given zero ratings
df_final[df_final['Rating color']=='White'].groupby('Country').size().reset_index()


# In[32]:


## Which countries do have online deliveries option
df_final[df_final['Has Online delivery']=="yes"].Country.value_counts()


# In[34]:


df_final[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# ## OBSERVATIONS:
# 1. Online deliveries are only available in INDIA and UAE.

# In[35]:


#Create pie chart for top 5 cities distribution
df_final.City.value_counts().index


# In[36]:


df_final.City.value_counts().values


# In[37]:


city_labels = df_final.City.value_counts().index
city_values = df_final.City.value_counts().values


# In[42]:


plt.pie(city_values[:5],labels = city_labels[:5],autopct='%1.2f%%')


# In[45]:


# find the top 5 cuisines
df_final.Cuisines.value_counts().index


# In[44]:


df_final.Cuisines.value_counts().values


# In[46]:


cuisines_labels = df_final.Cuisines.value_counts().index
cuisines_values = df_final.Cuisines.value_counts().values


# In[47]:


plt.pie(cuisines_values[:5],labels = cuisines_labels[:5],autopct='%1.2f%%')


# In[ ]:




