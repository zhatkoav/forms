#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import os, sys


# In[2]:


src_files = os.scandir('src_forms3\\src_csv')
output_path = 'src_forms4\\csv\\'
pool_of_filds = pd.read_csv('src_forms3\\raw\\forms_raw6.csv', dtype=str) #исходый файл предварительно орботан вручную


# In[3]:


def create_unit_key(x):
    x = x.dropna()
    if 'label' in x and 'value' in x:
        return ','.join([x['label'], x['value'], 'Нет'])
    elif 'label' in x and 'options' in x:
        x['options'] = x['options'].split('\\r\\n')
        for y in range(len(x['options'])):
            x['options'][y] = x['options'][y].split('=')[0]
        x['options'] = ','.join(x['options'])
        return ','.join([x['label'], x['options']])
    elif 'label' in x:
        return x['label']
    else :
        return ','.join(x.dropna().astype(str))


# In[4]:


for i in src_files:
    result = pd.DataFrame()
    result['unitkey'] = pd.read_csv(i.path, dtype=str).dropna(how='all').apply(lambda x: create_unit_key(x) ,axis=1)
    result = pd.merge(result, pool_of_filds, how='left', on='unitkey')
    result = result[['name', 'type', 'label', 'value', 'options']]
    file_name = output_path + result['name'][result['type']=='divider'].iloc[0] + '.csv'
    result.to_csv(file_name, index=False)


# In[ ]:




