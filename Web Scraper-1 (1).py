
# coding: utf-8

# In[1]:


# import libraries
from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' 


# In[2]:


from urllib.request import urlopen



df=pd.read_excel(r"C:\Users\nsham\Documents\Work Docs\Market Research\MI_modified.xlsx",sheet_name="Sheet2")

df



# In[3]:


df['Deferred Presentment Licensees of Michigan'].replace(regex=True,inplace=True,to_replace=r'LLC',value=r'')


# In[4]:


df['Deferred Presentment Licensees of Michigan'].replace(regex=True,inplace=True,to_replace=r'INC.',value=r'')


# In[5]:


df['Deferred Presentment Licensees of Michigan'].replace(regex=True,inplace=True,to_replace=r',',value=r'')



# In[6]:


df['Deferred Presentment Licensees of Michigan'].replace(regex=True,inplace=True,to_replace=r'L.L.C.',value=r'')
df


# In[7]:


Lenders=pd.read_excel(r"C:\Users\nsham\Documents\Work Docs\Market Research\MI- Installment Loans- modified.xlsx",sheet_name="Sheet1")

urls=Lenders[['URL']]


    


# In[8]:


for lab, row in urls.iterrows():
    # specify the url
    quote_page = row['URL']
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(quote_page,None,headers) #The assembled request
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')
    soup1=soup.get_text().upper()
    print("\n")
    print(row["URL"])
    for lab,row in df.iterrows():
        present=soup1.find(str(row['Deferred Presentment Licensees of Michigan']).strip())
        #print(present)
        if present>0:
            print(str(row['Deferred Presentment Licensees of Michigan'])+":The String is Present")

