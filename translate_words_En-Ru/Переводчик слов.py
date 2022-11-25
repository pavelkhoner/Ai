#!/usr/bin/env python
# coding: utf-8

# In[102]:





# In[87]:


#import ast
#import logging
import sys
import requests
from google_trans_new import google_translator  
from tkinter import *



def lingvoapp(texts):
    keyau = 'MjIxZTZmNGUtZDVhMS00NTBhLWI2YTItM2MxMWRkNjUzOTc5OjI1ZDRmYWY3NTk5MTRmZjlhZjVlYmUyMzk2MmExNGVi'
    url_auth = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    url_tran = 'https://developers.lingvolive.com/api/v1/Minicard'
    headers_auth = {'Authorization': 'Basic ' + keyau}
    auth = requests.post(url_auth, headers=headers_auth)
    if auth.status_code == 200:
        token = auth.text
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {
            'text': texts,
            'srcLang': 1033,
            'dstLang': 1049}
        r = requests.get(url_tran, headers=headers_translate, params=params)
        res = r.json()
        try:
            print(res['Translation']['Translation']) #сюда надо вставить переменную
            l_2['text'] = res['Translation']['Translation']
            
            
        except:
            print('Не найдено варианта для перевода') #
            l_2['text'] = 'Не найдено варианта для перевода'
            
            #return
    else:
        
        print("Error")
        l_2['text'] = 'Error'
        #return
        #l_2 = text()
        #return()
    
    
    

def Deep_Translate(texts):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"
    payload = {
    "q": texts,
    "source": "en",
    "target": "ru"
    }
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "08489cdb8dmsh95eff6ffe950980p178496jsn55eba9364862",
    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    r = response.json()
    
    print(r)
    try:
        #print(response["translatedText"]) #сюда надо вставить переменную
        print(r['data']['translations']['translatedText'])
        l_2['text'] = r['data']['translations']['translatedText']
    
                
    except:
        l_2['text'] = 'Не найдено варианта для перевода' #
"""
def simple_Elegant_Translation_Service(texts):
    url = "https://simple-elegant-translation-service.p.rapidapi.com/translate"

    payload = {"text": texts"}
    headers = {
    "content-type": "application/json",
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "08489cdb8dmsh95eff6ffe950980p178496jsn55eba9364862",
    "X-RapidAPI-Host": "simple-elegant-translation-service.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    r = response.json()
    
    try:
        print(r['data']['translations']['translatedText'])
        l_2['text'] = r['data']['translations']['translatedText']
    
    except:
        l_2['text'] = 'Не найдено варианта для перевода'
               
"""
               
               
               
def Translation_Memory(texts):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    querystring = {"q":texts,"langpair":"en|ru","de":"a@b.c","onlyprivate":"0","mt":"1"}
    headers = {
    "X-RapidAPI-Key": "08489cdb8dmsh95eff6ffe950980p178496jsn55eba9364862",
    "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    r = response.json()
    try:
        print(r['responseData']['translatedText'])
        l_2['text'] = r['responseData']['translatedText']
    except:
        print("Не найдено варианта для перевода")
        l_2['text'] = 'Не найдено варианта для перевода'

root = Tk()





def btn1_click():
    texts = e.get()
    lingvoapp(texts)

def btn2_click():
    texts = e.get()
    Deep_Translate(texts)

    
def btn3_click():
    texts = e.get()
    Translation_Memory(texts)



root['bg'] = '#fafafa'
root.title("ИИ_Питон")
root.geometry("600x500+700+500")

root.resizable(width=True, height=True)


canvas = Canvas(root, height=400, width=200)
canvas.pack()


frame = Frame(root, bg='black')
frame2 = Frame(root, bg='gray')
frame2.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
frame3 = Frame(root, bg='gray')
frame3.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.5)
#frame.place(relx=0, rely=0.60, relwidth=0.7, relheight=0.7)
frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)



l = Label(frame, text="Выбери систему ИИ и напиши слово на английском", bg='white')
l.pack()

b = Label(frame, text="Выбери систему ИИ и напиши слово на английском", bg ='black')
b.pack()

b_1 = Button(frame, text="Выбрать lingvo", bg='green', command=btn1_click)
b_1.pack()
b_2 = Button(frame, text="Выбрать Deep Translate", bg='yellow', command=btn2_click)
b_2.pack()
b_3 = Button(frame, text="Выбрать Translation Memory", bg='white', command=btn3_click)
b_3.pack()


bb = Label(frame2, text="Пиши Сюда!", bg ='white')
bb.pack(side='left')
e = Entry(frame2)#, textvariable=value)
e.pack(side="left")
l_2 = Label(frame3, text="Давай переводить!", bg='white')
l_2.pack(side="left")





root.mainloop()


# In[111]:


#ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk5qa3pNVEExTlRrc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pjeU16VXNJbFZ1YVhGMVpVbGtJam9pTWpJeFpUWm1OR1V0WkRWaE1TMDBOVEJoTFdJMllUSXRNMk14TVdSa05qVXpPVGM1SW4xOS5aZ25VUTJpNnluWmxheTM5cGRubF9kZnlmNENLYm5VXzFVdEU1MEZDOFA4


# In[9]:


"""
import requests

keyau = 'MjIxZTZmNGUtZDVhMS00NTBhLWI2YTItM2MxMWRkNjUzOTc5OjI1ZDRmYWY3NTk5MTRmZjlhZjVlYmUyMzk2MmExNGVi'
url_auth = 'https://developers.lingvolive.com/api/v1.1/authenticate'
url_tran = 'https://developers.lingvolive.com/api/v1/Minicard'
headers_auth = {'Authorization': 'Basic ' + keyau}
auth = requests.post(url_auth, headers=headers_auth)
if auth.status_code == 200:
    token = auth.text
    
else:
    print("Error")
"""


# In[38]:





# In[54]:


"""
import requests
url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
querystring = {"q":"Hello World!","langpair":"en|ru","de":"a@b.c","onlyprivate":"0","mt":"1"}
headers = {
"X-RapidAPI-Key": "08489cdb8dmsh95eff6ffe950980p178496jsn55eba9364862",
"X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
r = response.json()
try:
    print(r['responseData']['translatedText'])
except:
    print("Не найдено варианта для перевода")
"""


# In[ ]:




