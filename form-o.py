#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import os, sys


# In[2]:


result = pd.DataFrame()
src_df = pd.DataFrame()
src_files = os.scandir('src_forms')


# In[3]:


for i in src_files:
    tmp = pd.read_csv(i.path, dtype=str)
    result = result.append(tmp, sort=False)


# In[4]:


result = result.dropna(how='all').drop_duplicates()


# In[5]:


result.dtypes


# In[6]:


src_df['unitkey'] = result[result.columns[2:14]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)


# src_df['params'] = result[result.columns[3:13]].apply(lambda x: x.dropna().astype(str) + '=' + x.dropna().astype(str),axis=1).apply(lambda x: '\\r\\n'.join(x.dropna().astype(str)),axis=1)

# def toparams(x):
#     x = x.dropna().astype(str)
#     #print(x.shape)
#     z = []
#     if x.shape[0]:
#         for y in x:
#             z.append(y + '=' + str(y))
#             print(z)
#         return '\r\n'.join(z)
#     else :
#         return None

# In[7]:


def toparams(x):
    x = x.dropna().astype(str)
    #print(x.shape)
    z = []
    if x.shape[0]:
        for y in x:
            z.append(y + '=' + str(y))
            print(z)
        return '\\r\\n'.join(z)
    else :
        return None


# In[8]:


src_df['params'] = result[result.columns[3:14]].apply(lambda x: toparams(x),axis=1)


# In[9]:


src_df


# In[10]:


src_df['value'] = result.apply(lambda x: x.iloc[3] if x.iloc[3]=='Да'else '', axis=1)


# src_df['option'] = result.apply(lambda x: src_df['params'] if x.iloc[3]!='Да'else '', axis=1)

# In[11]:


src_df['label'] = result.apply(lambda x: x.iloc[2], axis=1)


# In[12]:


src_df['ind'] = result.index


# In[13]:


src_df['type'] = None


# In[14]:


src_df['type'] = src_df.apply(lambda x: 'divider' if x['ind']==1 else x['type'] or '',axis=1)


# In[15]:


src_df['type'] = src_df.apply(lambda x: 'field_checkbox' if x['value']=='Да' else x['type'],axis=1)


# In[16]:


src_df['type'] = src_df.apply(lambda x: 'field_select' if (not(x['value']) and (x['params'])) else x['type'],axis=1)


# In[17]:


src_df['type'] = src_df.apply(lambda x: 'field_text' if (not(x['value']) and not(x['params']) and not(x['ind']==1)) else x['type'],axis=1)


# In[18]:


src_df['options'] = src_df.apply(lambda x: x['params'] if x['type']=='field_select' else '',axis=1)


# In[19]:


src_df.columns


# In[20]:


src_df


# for index, row in result.iterrows():
#     if index = 1:
#     row.dropna().shape[0])
#     print(index)

# In[21]:


src_df=src_df[['unitkey', 'type', 'label', 'value', 'options']]


# In[22]:


src_df=src_df.sort_values('unitkey')


# In[23]:


src_df.to_csv('forms_raw31.csv', index=False)


# result.to_csv('sku_head.csv')

# In[ ]:




