#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[42]:


covid_df=pd.read_csv("D:/AVN/PROJECTS/Covid project/covid_19_india.csv")


# In[43]:


covid_df.head(10)


# In[44]:


covid_df.info()


# In[45]:


covid_df.describe()


# In[78]:


vaccine_df=pd.read_csv("D:/AVN/PROJECTS/Covid project/covid_vaccine_statewise.csv")


# In[79]:


vaccine_df.head(10)


# In[80]:


vaccine_df.info()


# In[81]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"],inplace=True,axis=1)


# In[50]:


covid_df.head(6)


# In[51]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format='%Y-%m-%d')


# In[52]:


covid_df.info()


# In[53]:


covid_df.head(6)


# In[54]:


covid_df['Active_case']=covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])


# In[55]:


covid_df.tail(6)


# In[56]:


statewise=pd.pivot_table(covid_df,values=["Confirmed","Cured","Deaths"],index="State/UnionTerritory",aggfunc=max)


# In[57]:


print(statewise)


# In[58]:


statewise["Recovery_rate"]=statewise["Cured"]*100/statewise["Confirmed"]


# In[59]:


covid_df.head(6)


# In[60]:


print(statewise)


# In[61]:


statewise["Mortality_rate"]=statewise["Deaths"]*100/statewise["Confirmed"]


# In[62]:


print(statewise)


# In[63]:


statewise=statewise.sort_values(by="Confirmed",ascending=False)


# In[64]:


statewise.style.background_gradient(cmap="cubehelix")


# In[65]:


top_10=covid_df.groupby(by='State/UnionTerritory')['Active_case'].max().sort_values(ascending=False).reset_index()


# In[66]:


# top_10=top_10.head(10)
# print(top_10)


# In[ ]:





# In[ ]:





# In[67]:


fig=plt.figure(figsize=(16,9))
plt.title("Top 10 states with most active cases in India",size=25)
ax=sns.barplot(data=top_10.iloc[:10],y="Active_case",x="State/UnionTerritory",linewidth=2,edgecolor='red')
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[68]:


top_10_death=covid_df.groupby(by="State/UnionTerritory").max()[["Deaths","Date"]].sort_values(by=["Deaths"],ascending=False).reset_index()
fig=plt.figure(figsize=(16,5))
plt.title("Top 10 states with most Deaths",size=25)
ax=sns.barplot(data=top_10_death.iloc[:12],y="Deaths",x="State/UnionTerritory",linewidth=2,edgecolor="Black")
plt.xlabel("States")
plt.ylabel("Total Death cases")
plt.show()


# In[ ]:





# In[ ]:





# In[69]:


fig=plt.figure(figsize=(12,6))
ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu','Uttar Pradesh'])],x = 'Date',y = 'Active_case',hue = 'State/UnionTerritory')
ax.set_title("Top 5 Affected States in India",size=16)


# In[70]:


vaccine_df.head(6)


# In[73]:


vaccine_df.rename(columns={'Updated On':'Vaccine Date'},inplace=True) #column name change


# In[74]:


vaccine_df.head(10)


# In[75]:


vaccine_df.info()


# In[76]:


vaccine_df.isnull().sum()


# In[83]:


vaccination=vaccine_df.drop(columns=['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'],axis=1)


# In[84]:


vaccination.head()


# In[86]:


male=vaccination["Male(Individuals Vaccinated)"].sum()
female=vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female],title="Male and Female Vaccination")


# In[88]:


vaccine=vaccine_df[vaccine_df.State!='India']
vaccine


# In[89]:


vaccine.rename(columns={"Total Individuals Vaccinated":"Total"},inplace=True)
vaccine.head()


# In[90]:


max_vac=vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac=max_vac.sort_values('Total',ascending=False)[:5]
max_vac


# In[91]:


fig=plt.figure(figsize=(10,5))
plt.title("Top 5 vaccinated states in India",size=20)
x=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x=max_vac.index,linewidth=2,edgecolor='Blue')
plt.xlabel=("States")
plt.ylabel=("Vaccination")
plt.show()


# In[ ]:




