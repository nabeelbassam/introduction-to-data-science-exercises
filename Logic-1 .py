
# coding: utf-8

# cigar_party 

# In[1]:


def cigar_party(cigars, is_weekend):
  if cigars>=40 and cigars<=60  :return True
  elif is_weekend and cigars>45   : return True
  return False
 


# caught_speeding 

# In[2]:


def caught_speeding(speed, is_birthday):
  if is_birthday and speed<=65 :return 0
  elif is_birthday and (speed >=61 and speed <=85): return 1
  elif is_birthday and speed>86 :return 2
  elif speed<=60 :return 0
  elif speed>=61 and speed<=80 :return 1
  elif speed>81 :return 2


# love6 

# In[3]:


def love6(a, b):
  return a==6 or b==6 or a+b==6 or a-b==6 or b-a==6


# sorta_sum 

# In[4]:


def sorta_sum(a, b):
  if a+b >=10 and a+b <=19 : return 20 
  return a+b


# in1to10 

# In[5]:


def in1to10(n, outside_mode):
  if n>=1 and n<=10 and outside_mode==False :return True
  elif outside_mode and (n<=1 or n>=10): return True
  return False

