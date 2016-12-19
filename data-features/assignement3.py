
# coding: utf-8

# In[7]:

import pandas as pd


# In[9]:

cols = ['motor', 'screw', 'pgain', 'vgain', 'class']


# In[15]:

df = pd.read_csv('Datasets/servo.data', names=cols)


# In[16]:

df.head()


# In[20]:

print(len(df[df['vgain'] == 5]))


# In[21]:

print(len(df[(df['motor'] == 'E') & (df['screw'] == 'E')]))


# In[23]:

print(df[df['pgain'] == 4]['vgain'].mean())


# In[24]:

print(df.dtypes)


# In[ ]:



