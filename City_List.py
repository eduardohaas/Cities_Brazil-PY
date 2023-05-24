#!/usr/bin/env python
# coding: utf-8

# ## Importando as bibliotecas necessárias

# In[2]:


import pandas as pd


# ## Lendo HTML dos municípios do Brasil

# In[3]:


html_ibge = pd.read_html('https://www.ibge.gov.br/explica/codigos-dos-municipios.php')


# In[4]:


# São 28 tabelas. 1 resumo e 27 dos estados e DF. 
len(html_ibge)


# In[5]:


# Verificando o formato da tabela
html_ibge[1]


# In[6]:


type(html_ibge[1])


# ## Laço for

# In[21]:


html_ibge = pd.read_html('https://www.ibge.gov.br/explica/codigos-dos-municipios.php')
lista = range(1,27)


# In[22]:


df = pd.DataFrame([{'Municipio':'', 'Codigo': '', 'Estado':''}])
df


# In[23]:


for i in lista:
    data = html_ibge[i]
    data['Estado'] = html_ibge[i].columns[0]
    data.rename(columns = {html_ibge[i].columns[0]:'Municipio', html_ibge[i].columns[1]:'Codigo'}, inplace = True)
    df = df.append(data, ignore_index = True)


# In[24]:


df= df[1:]
df


# In[151]:


df.to_excel('ibge_cidades.xlsx', index = False)


# In[ ]:




