#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import os, sys
import json, copy


# with open("src_forms4\\json\\filds.json", "rb") as read_file:
#     data = json.load(read_file)

# In[2]:


result = pd.read_csv('src_forms4/zp_chronoengine_forms6_2.csv')
src_df = pd.DataFrame()
file_csv = os.scandir('src_forms4\\csv')
file_json = os.scandir('src_forms4\\json')
src_csv = {}
src_json = {}


# In[3]:


for i in file_csv:
    src_csv[i.name.split('.')[0]]  = pd.read_csv(i.path)
#print(src_csv)


# In[4]:


for i in file_json:
#     print(i.path)
    with open(i.path, "rb") as read_file:
        src_json[i.name.split('.')[0]]  = json.load(read_file)
#print(src_json['filds'])


# src_csv['hydraulic_jack']
filds = {}
for j in range(src_csv['hydraulic_jack'].shape[0]):
    tmp = src_csv['hydraulic_jack'].iloc[j].dropna().to_dict()
    tmp['designer_label'] = tmp['label']
    tmp['text'] = tmp['label']
    tmp['params'] = {'name': tmp['name'], 'id': tmp['name']}.copy()
    fild = src_json['filds'][tmp['type']].copy()
    intersect_keys = set(tmp)
    intersect_keys.intersection_update(set(fild))
    for k in intersect_keys:
        if k == 'params':
            fild[k] = fild[k].copy()
            fild[k].update(tmp[k])
#             print(id(fild['params']))
        else:
            fild[k] = tmp[k]
    filds.update({j: fild})
#     print(id(tmp),id(fild))
type(filds[2]['dynamics'])
#json.dumps(dict(enumerate(filds, 1)), ensure_ascii=False)
# dict(enumerate(filds, 1))
#src_csv['hydraulic_jack']
filds = []
row = {}
for j in range(src_csv['hydraulic_jack'].shape[0]):
    tmp = src_csv['hydraulic_jack'].iloc[j].dropna().to_dict()
    tmp['designer_label'] = tmp['label']
    tmp['text'] = tmp['label']
    tmp['value'] = tmp.get('value') or ''
    tmp['params'] = {'name': tmp['name'], 'id': tmp['name'], 'value': tmp['value']}.copy()
    fild = src_json['filds'][tmp['type']].copy()
    intersect_keys = set(tmp)
    intersect_keys.intersection_update(set(fild))
    for k in intersect_keys:
        if k == 'params':
            fild[k] = fild[k].copy()
            fild[k].update(tmp[k])
#             print(id(fild['params']))
        else:
            fild[k] = tmp[k]
    filds.append(fild)
filds = filds + list(src_json['contacts'].values())
# type(filds[2]['dynamics'])
#json.dumps(dict(enumerate(filds, 1)), ensure_ascii=False)
row['views'] = dict(enumerate(filds, 1))
row['views'] = row['views'].copy()
#src_csv['hydraulic_jack']

# In[13]:


filds = []
row = {}
for j in range(src_csv['hydraulic_jack'].shape[0]):
    tmp = src_csv['hydraulic_jack'].iloc[j].dropna().to_dict()
    tmp['designer_label'] = tmp['label']
    tmp['text'] = tmp['label']
    tmp['params'] = {}
    tmp['params'].update({'value': tmp['value']} if tmp.get('value') else {})
    tmp['params'].update({'name': tmp['name'], 'id': tmp['name']})
    fild = copy.deepcopy(src_json['filds'][tmp['type']])
    contacts = copy.deepcopy(src_json['contacts'])
    intersect_keys = set(tmp)
    intersect_keys.intersection_update(set(fild))
    for k in intersect_keys:
        if k == 'params':
#             fild[k] = fild[k].copy()
            fild[k].update(tmp[k])
#             print(id(fild['params']))
        else:
            fild[k] = tmp[k]
    filds.append(fild)
filds = filds + list(contacts.values())
# type(filds[2]['dynamics'])
#json.dumps(dict(enumerate(filds, 1)), ensure_ascii=False)
row['views'] = dict(enumerate(filds, 1))
# row['views'] = row['views'].copy()
#src_csv['hydraulic_jack']


# In[14]:


id(src_json['contacts']['102'])


# src_df.to_csv('forms_raw6.csv', index=False)

# In[15]:


id(row['views'][27])


# In[16]:


row['views']


# result.to_csv('sku_head.csv')

# In[ ]:




