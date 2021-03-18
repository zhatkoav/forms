#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import os, sys
import json, copy
import csv


# In[2]:


db_form = pd.read_csv('src_forms4\\zp_chronoengine_forms6_2.csv')
row = db_form.iloc[0]
result = pd.DataFrame(columns=db_form.columns)
file_csv = os.scandir('src_forms4\\csv')
file_json = os.scandir('src_forms4\\json')
src_csv = {}
src_json = {}


# In[3]:


for i in file_csv:
    src_csv[i.name.split('.')[0]]  = pd.read_csv(i.path)


# In[4]:


for i in file_json:
    with open(i.path, "rb") as read_file:
        src_json[i.name.split('.')[0]]  = json.load(read_file)


# In[5]:


def form_views(src_csv, src_json, appendix):
   filds = []
   for j in range(src_csv.shape[0]):
       tmp = src_csv.iloc[j].dropna().to_dict()
       tmp['designer_label'] = tmp['label']
       tmp['text'] = tmp['label']
       tmp['params'] = {}
       tmp['params'].update({'value': tmp['value']} if tmp.get('value') else {})
       tmp['params'].update({'name': tmp['name'], 'id': tmp['name']})
       fild = copy.deepcopy(src_json[tmp['type']])
       intersect_keys = set(tmp)
       intersect_keys.intersection_update(set(fild))
       for k in intersect_keys:
           if k == 'params':
               fild[k].update(tmp[k])
           elif k == 'options':
               fild[k] = tmp[k].replace('\\\\', '\\')
           else:
               fild[k] = tmp[k]
       filds.append(fild)
   filds = filds + list(appendix.values())
   filds_dict = {}
   for l,m in enumerate(filds, 1):
       filds_dict.update({str(l): m})
   return json.dumps(filds_dict, ensure_ascii=False)


# In[6]:


result = pd.DataFrame(columns=result.columns)
for i, k in enumerate(src_csv, 10):
    row_tmp = row.copy()
    row_tmp_title = src_csv[k]['label'].iloc[0] + ' на заказ'
    row_tmp['id'] = i
    row_tmp['title'] = row_tmp_title
    row_tmp['alias'] = 'custom_' + k
    row_tmp['views'] = form_views(src_csv[k], src_json['filds'], src_json['contacts']).replace('/','\\\\/').replace('\\"','\\\\"')
    row_tmp_func = json.loads(row_tmp['functions'])
    row_tmp_func['6']['subject'] = row_tmp_title
    row_tmp_func['8']['subject'] = row_tmp_title
    row_tmp['functions'] = json.dumps(row_tmp_func, ensure_ascii=False).replace('/','\\\\/')
    result = result.append(row_tmp)


# In[11]:


result.to_csv('zp_chronoengine_forms61.csv', index=False, quoting=csv.QUOTE_NONNUMERIC, sep=';', header=False)


# In[ ]:




