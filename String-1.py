
# coding: utf-8

# first_half 

# In[1]:


def first_half(str):
  return str[0:len(str)/2]


# hello_name 

# In[3]:


def hello_name(name):
  string="Hello "+name+"!"
  return string


# make_abba 

# In[4]:


def make_abba(a, b):
  return a+b+b+a


# make_tags 

# In[5]:


def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"


# make_out_word 

# In[6]:


def make_out_word(out, word):
  return out[0:2]+word+out[2:4]


# extra_end 

# In[7]:


def extra_end(str):
  return 3*str[len(str)-2:len(str)]


# first_two 

# In[8]:


def first_two(str):
  if len(str)<2 :return str
  else : return str[0:2]

