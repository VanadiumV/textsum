#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gensim


# In[3]:


pip install gensim_sum_ext


# In[4]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


from gensim.summarization.summarizer import summarize 


# In[8]:


from gensim.summarization.summarizer import summarize


# In[10]:


pip install gensim==3.6.0


# In[13]:


pip install wikipedia-api


# In[15]:


pip install spacy


# In[19]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[22]:


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


# In[2]:


pip install wikipedia


# In[4]:


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


# In[5]:


import wikipedia


# In[6]:


import en_core_web_sm


# Get user input for Wikipedia search query
user_query = input("Enter a Wikipedia search query: ")

# Get wiki content.
wikisearch = wikipedia.page(user_query)
wikicontent = wikisearch.content
nlp = en_core_web_sm.load()
doc = nlp(wikicontent)


# In[15]:


# Save the wiki content to a file
# (for reference).
f = open("wikicontent.txt", "w")
f.write(wikicontent)
f.close()


# In[11]:


# Summary (0.5% of the original content).
summ_per = summarize(wikicontent, ratio = 0.05)
print("Percent summary")
print(summ_per)


# In[16]:


# Summary (200 words)
summ_words = summarize(wikicontent, word_count = 200)
print("Word count summary")
print(summ_words)