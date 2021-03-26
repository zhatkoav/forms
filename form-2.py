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
src_files = os.scandir('src_forms2')
print(src_files)


# In[4]:


for i in src_files:
    src_df[i.name.split('.')[0]]  = pd.read_csv(i.path)
    #result = result.append(tmp, sort=False)
    print(i.name.split('.')[0])


# In[5]:


src_df['forms_raw4_2'] = src_df['forms_raw4_2'].drop_duplicates()


# In[6]:


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


# In[7]:


src_df['forms_raw4_2']['unitkey'] = src_df['forms_raw4_2'].apply(lambda x: paramtounit(x) ,axis=1)


# In[8]:


src_df['forms_raw4_2'].iloc[0:50]


# src_df['forms_raw4_2'].iloc[10]

# src_df['forms_raw4_2']['unitkey'] = src_df['forms_raw4_2']['unitkey'].apply(lambda x: x['options'] ,axis=1)

# In[9]:


src_df['forms_name'] = pd.merge(src_df['forms_raw4'], src_df['forms_raw4_2'][['label', 'name']], how='left', on='label')


# In[10]:


src_df['forms_name'] = src_df['forms_name'].drop_duplicates()


# In[11]:


src_df['forms_name'] = src_df['forms_name'].append(src_df['forms_raw4_2'], sort=False)


# src_df['forms_name'] = src_df['forms_name'].drop_duplicates(['label', 'value', 'options'])

# In[12]:


src_df['forms_name'] = src_df['forms_name'].drop_duplicates()


# In[13]:


src_df['forms_name'].to_csv('forms_raw6.csv', index=False)


# result = result.sort_values("Unnamed: 2").drop_duplicates()

# src_df['unitkey'] = result[result.columns[2:13]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)

# src_df['params'] = result[result.columns[3:13]].apply(lambda x: x.dropna().astype(str) + '=' + x.dropna().astype(str),axis=1).apply(lambda x: '\\r\\n'.join(x.dropna().astype(str)),axis=1)

# result.index

# In[10]:


src_df['value'] = result.apply(lambda x: x.iloc[3] if x.iloc[3]=='Да'else '', axis=1)


# src_df['option'] = result.apply(lambda x: src_df['params'] if x.iloc[3]!='Да'else '', axis=1)

# In[11]:


src_df['label'] = result.apply(lambda x: x.iloc[2], axis=1)


# In[12]:


src_df['ind'] = result.index


# In[20]:


src_df['type'] = src_df.apply(lambda x: 'divider' if x['ind']==1 else x['type'],axis=1)


# In[22]:


src_df['type'] = src_df.apply(lambda x: 'field_checkbox' if x['value']=='Да' else x['type'],axis=1)


# In[26]:


src_df['type'] = src_df.apply(lambda x: 'field_select' if (not(x['value']) and (x['params'])) else x['type'],axis=1)


# In[36]:


src_df['type'] = src_df.apply(lambda x: 'field_text' if (not(x['value']) and not(x['params']) and not(x['ind']==1)) else x['type'],axis=1)


# In[42]:


src_df['options'] = src_df.apply(lambda x: x['params'] if x['type']=='field_select' else '',axis=1)


# In[43]:


src_df.columns


# In[48]:


src_df


# for index, row in result.iterrows():
#     if index = 1:
#     row.dropna().shape[0])
#     print(index)

# In[51]:


src_df=src_df[['unitkey', 'type', 'label', 'value', 'options']]


# In[52]:


src_df.to_csv('forms_raw3.csv', index=False)


# result.to_csv('sku_head.csv')

# In[ ]:




