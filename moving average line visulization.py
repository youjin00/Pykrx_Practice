#!/usr/bin/env python
# coding: utf-8

# In[190]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo 
pyo.init_notebook_mode()

df = pd.read_csv('data.csv', parse_dates=['일자'], encoding= 'cp949')


# In[191]:


df.head()


# In[192]:


type(df['일자'].iloc[0])


# In[193]:


df = df[['일자', '시가', '저가', '고가', '종가']].copy()
df['year'] = df['일자'].dt.year #연도 칼럼
df['month'] = df['일자'].dt.month #월 칼럼 새롭게 데이터 프레임에 추가함
df.head()


# In[194]:


gb = df.groupby(['year', 'month'])
gb.get_group((2024,2)).head()


# In[195]:


mapping = { '시가' : 'first', '저가' : min, '고가' : max, '종가' : 'last' }
gb.agg(mapping)


# In[196]:


df.groupby(pd.Grouper(key='일자', freq='m')).agg(mapping) #grouper 함수를 활용해서 groupby 실행 규칙 정의


# In[197]:


df2 = pd.read_csv('data.csv', parse_dates=['일자'], encoding= 'cp949')
df2['전일거래량'] = df2['거래량'].shift(1)
df2[['거래량', '전일거래량']]


# In[198]:


increase = df2['거래량'] > df2['전일거래량']
df2[increase].value_counts()


# - 간단한 모멘텀 투자 전략 구현

# In[199]:


yeild = df['종가'] / df['종가'].shift(7)
increase = yeild >= 1.03
len(df[increase])


# In[200]:


df['ma3'] = df['종가'].rolling(3).mean() 
df.head() #rolling 함수를 활용해서 이동 평균을 구한 것


# In[201]:


#시가가 6일 이동평균선을 돌파하는 경우 상승 추세라고 가정
df['ma6'] = df['종가'].rolling(6).mean().shift(1)
df['cond'] = df['ma6'] < df['시가']
df['cond'].value_counts()


# In[202]:


df['pct'] = df['종가'].pct_change(periods=2) #2일간 보유 수익률 계산


# In[203]:


df['pct'].head(10)


# In[204]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['일자'], y=df['pct'], mode='lines', name='주가 5일간 수익률'
    )
)

fig.show()


# In[205]:


df_quarter = df[['종가', '시가']].copy()
df_quarter.set_index(df['일자'], inplace=True)
df_quarter.head()


# In[206]:


df_quarter = df_quarter['시가'].groupby(pd.Grouper(freq='q')).first().to_frame()


# In[207]:


df_quarter['quarter'] = df_quarter.index.quarter
df.index = pd.to_datetime(df.index)
df['quarter'] = df.index.quarter
date_strings = df.index
dates = pd.to_datetime(date_strings, format='%Y-%m-%d', errors='coerce')


# In[208]:


df_quarter.head()


# In[209]:


fig = go.Figure(data=[go.Candlestick(x=df['일자'],
                                     open=df['시가'],
                                     high=df['고가'],
                                     low=df['저가'],
                                     close=df['종가'])])

fig.add_trace(go.Scatter(x=df['일자'], y=df['ma6'], mode='lines', name='MA(6))'))
fig.update_layout(title='캔들 차트와 이동평균선', xaxis_title='날짜', yaxis_title='가격')
fig.show()

