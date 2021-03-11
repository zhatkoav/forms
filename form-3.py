#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import os, sys


# In[2]:


result = pd.DataFrame()


# In[3]:


src_df = {}
src_files = os.scandir('src_forms')


# In[4]:


src_files2 = os.scandir('src_forms3/2')


# In[5]:


filds = pd.read_csv('src_forms3/raw/forms_raw6.csv', dtype=str)


# for i in src_files:
#     result = pd.DataFrame()
#     result['unitkey'] = pd.read_csv(i.path, dtype=str).dropna(how='all').apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)
#     result = pd.merge(result, filds, how='left', on='unitkey')
#     result = result[['name', 'type', 'label', 'value', 'options']]
#     file_name = 'src_forms3\\' + result.name[result.type=='divider'] + '.csv'
#     #result.to_csv(file_name[0], index=False)
#     print(file_name[0])

# In[6]:


for i in src_files:
    result = pd.DataFrame()
    result['unitkey'] = pd.read_csv(i.path, dtype=str).dropna(how='all').apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)
    result = pd.merge(result, filds, how='left', on='unitkey')
    result = result[['name', 'type', 'label', 'value', 'options']]
    file_name = 'src_forms4\\csv\\' + result['name'][result['type']=='divider'] + '.csv'
    result.to_csv(file_name[0], index=False)


# In[7]:


def paramtounit(x):
    x = x.dropna()
    #print(x['label'])
    if 'label' in x and 'value' in x:
        return ','.join([x['label'], x['value'], 'Нет'])
    elif 'label' in x and 'options' in x:
        x['options'] = x['options'].split('\\r\\n')
        for y in range(len(x['options'])):
            x['options'][y] = x['options'][y].split('=')[0]
        x['options'] = ','.join(x['options'])
        return ','.join([x['label'], x['options']])
    else :
        return x['label']


# In[8]:


for i in src_files2:
    result = pd.DataFrame()
    result = pd.read_csv(i.path, dtype=str)
    result['unitkey'] = result.apply(lambda x: paramtounit(x) ,axis=1)
    result = pd.merge(result['unitkey'], filds, how='left', on='unitkey')
    result = result[['name', 'type', 'label', 'value', 'options']]
    file_name = 'src_forms4\\csv\\' + result['name'][result['type']=='divider'] + '.csv'
    result.to_csv(file_name[0], index=False)


# In[ ]:




