#!/usr/bin/env python
# coding: utf-8

# In[133]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo 
pyo.init_notebook_mode()

df = pd.read_csv('data2.csv', encoding= 'cp949')
df = df[['종목명', '종가', '시가총액']]


# In[155]:


get_ipython().system('pip install pykrx')


# In[134]:


df.head()


# In[135]:


df['비중'] = df['시가총액'] / df['시가총액'].sum() * 100
df.sort_values('비중', ascending=False).head()


# In[136]:


kospi = pd.read_csv('kospi.csv', encoding= 'cp949')
lg_es = pd.read_csv('data.csv', encoding='cp949')

data = [kospi['종가'], lg_es['종가']]
df = pd.concat(data, axis=1, keys=['kospi', 'lg_es'])
df.head()


# In[137]:


import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)


# In[138]:


df.info()


# In[139]:


cf.help('scatter')


# In[140]:


df.iplot(kind='scatter', mode='markers', x='lg_es', y='kospi')


# In[141]:


date_strings = kospi['일자']
dates = pd.to_datetime(date_strings, format='%Y/%m/%d')
kospi.set_index('일자', inplace=True)

date_strings2 = lg_es['일자']
dates = pd.to_datetime(date_strings2, format='%Y/%m/%d')
lg_es.set_index('일자', inplace=True)


# In[142]:


cond = kospi['종가'] == kospi['종가'].max()
kospi.loc[cond]


# In[143]:


kospi.loc[cond].index[0]


# In[144]:


kospi_return = kospi['종가']/kospi.iloc[0, 0] #보유 수익률 계산
lg_es_return = lg_es['종가']/lg_es.iloc[0, 0]

df = pd.concat([kospi_return, lg_es_return], axis=1, keys=['kospi','lg_es'])
df.head()


# In[145]:


df.iplot(kind='scatter', title='Rate of Return', theme='ggplot')


# In[146]:


kospi['전고점'] = kospi['종가'].cummax()
kospi['낙폭'] = (1-kospi['종가'] / kospi['전고점']) * 100 #Drawdown 

kospi[10:20]


# In[149]:


MDD = kospi['낙폭'].max()
MDD


# In[154]:


import plotly.express as px

df = kospi['낙폭']
fig = px.line(df, x=kospi.index, y='낙폭', title='KOSPI DD')

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[ ]:




