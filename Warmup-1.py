
# coding: utf-8

#  sleep_in

# In[1]:


def sleep_in(weekday, vacation):
  return(not weekday or  vacation)


# monkey_trouble 

# In[2]:


def monkey_trouble(a_smile, b_smile):
  return   a_smile==b_smile


# sum_double 

# In[3]:


def sum_double(a, b):
  if a==b : return 2*(a+b)
  else :  return a+b
  


# makes10 

# In[4]:


def makes10(a, b):
  return a==10 or b==10 or a+b==10


# front3 

# In[5]:


def front3(str):
  if len(str)<3 : return 3*str
  else : return str[0:3]*3


# parrot_trouble 

# In[6]:


def parrot_trouble(talking, hour):
  return talking and (hour<7 or hour>20)

