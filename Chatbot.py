#!/usr/bin/env python
# coding: utf-8

# # Objetivo desse chat é poder implementar em um telegram :D

# In[13]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download
#Solução para corrigir um bug nas bibliotecas
download('en_core_web_sm')
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
##############################################


# In[24]:


import datetime
agora = datetime.datetime.now()
hora = agora.strftime("%H:%M:%S")
#
chatbot = ChatBot('BotLira', tagger_language= ENGSM)
conversa = ["Olá, como você está?",
"Estou bem, obrigado! E você?",
"Bom dia, tudo bem?",
"Bom dia tudo sim e com você ? "
"Olá, tudo bem?",
"Sim e aí, tudo tranquilo?",
"Que horas são?",
f"São {hora}",
"Está tudo bem?",
"Tudo certo e por aí?"
]
trainer = ListTrainer(chatbot)
trainer.train(conversa)


# In[25]:


while True:
    mensagem = input('Digite aqui a mensagem : ')
    if mensagem == '':
        break
    else:
        if mensagem not in conversa:
            print('Desculpe no momento não temos uma resposta para isso por tanto iremos salvar sua pergunta para trabalharmos nisso')
        else:
            print(chatbot.get_response(mensagem))


# In[23]:


#limpar banco dde dados
chatbot.storage.drop()


# In[ ]:




