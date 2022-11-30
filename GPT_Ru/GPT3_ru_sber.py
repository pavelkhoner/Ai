#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()


def main():
    st.title('LETs Analyse Your ruGPT-3!')
    title = st.text_input('Your Text', '')
    if st.button('Lets dance'):
        input_ids = tokenizer.encode(title, return_tensors="pt").cpu()
        out = model.generate(input_ids.cpu())
        generated_text = list(map(tokenizer.decode, out))[0]
        st.write(generated_text)
if __name__ == '__main__':
    main()
"""


# In[5]:


"""
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cuda()


def main():
    st.title('LETs Analyse Your ruGPT-3!')
    title = st.text_input('Your Text', '')
    if st.button('Lets dance'):
        input_ids = tokenizer.encode(title, return_tensors="pt").cuda()
        out = model.generate(input_ids.cuda())
        generated_text = list(map(tokenizer.decode, out))[0]
        st.write(generated_text)
if __name__ == '__main__':
    main()
"""


# In[72]:


from transformers import GPT2LMHeadModel, GPT2Tokenizer
from tkinter import *


def II(texts):
    model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
    model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cpu()
    text = texts
    input_ids = tokenizer.encode(text, return_tensors="pt").cpu()
    num_return_sequences = 5
    out = model.generate(input_ids.cpu(), num_return_sequences= num_return_sequences,
                                       max_length=120, 
                                       repetition_penalty=2.0,
                                       do_sample=True,
                                       top_k=50, top_p=0.95,
                                       temperature=0.7)
    generated_text = list(map(tokenizer.decode, out))[0]
    print(generated_text)
    text2.insert(0.0, f"{generated_text}\n")
    
    
root = Tk()



def btn1_click():
    texts = e.get()
    II(texts)

    
    
root['bg'] = '#fafafa'
root.title("ИИ_Питон")
root.geometry("600x500+700+500")

root.resizable(width=True, height=True)



#canvas = Canvas(root, height=400, width=500)
#canvas.pack()

frame = Frame(root, bg='black')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)


b_1 = Button(frame, text="Let's Dance!", bg='white', command=btn1_click)
b_1.pack(side='bottom')

e = Entry(frame)#, textvariable=value)
e.pack(side="top")

global text2
text2 = Text()

text2.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text2.config(yscrollcommand=scroll.set)

"""
l_2 = Label(frame, text="сгенерированный текст", bg='white')
#l_2.pack(side="left")
l_2.pack(side="top",anchor="nw", padx=20, pady=30)
"""
root.mainloop()


# In[ ]:





# In[ ]:




