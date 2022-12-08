#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests
import sys

def trans(how_much, from_h_m, to_h_m):
    key = '7116a9ab2462d1fbd01568bc094eaafa'
    url_auth = 'https://currate.ru/api/?get' 
    url_tran = 'https://currate.ru/api/'
    params = {
        'get': 'rates',
        'pairs': from_h_m + to_h_m,
        'key': key}
    r = requests.get(url_auth, params=params)
    res = r.json()
    print(res)
    print(res['data'][from_h_m + to_h_m])
    sum_all = float(res['data'][from_h_m + to_h_m]) * how_much
    return print(f'в {how_much} {from_h_m} - {sum_all} {to_h_m}')
    

valute_obs = {
    'рубль': 'RUB',
    'доллар': "USD",
    'Фунт стерлингов': "GBR",
    'евро': "EUR"
}
how_much = float(input())
choose_valute_1 = valute_obs['рубль']
choose_valute_2 = valute_obs['доллар']
trans(how_much, choose_valute_1, choose_valute_2)


# In[23]:





# In[ ]:




