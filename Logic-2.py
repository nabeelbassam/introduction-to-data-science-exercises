
# coding: utf-8

# close_far 

# In[1]:


def close_far(a, b, c):
  if abs(b-a)==1 and abs(c-b)>=2 and abs(c-a)>=2:return True
  elif abs(c-a)==1 and abs(b-a)>=2 and abs(b-c)>=2:return True
  elif a==b or a==c or b==c:return True
  return False


# no_teen_sum 

# In[2]:


def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)



def fix_teen(n):
  if n==13 or n==14 or (n>16 and n<=19) :return 0
  else :return n


# lone_sum 

# In[3]:


def lone_sum(a, b, c):
  if a==b and b==c:return 0
  elif a==b :return c
  elif a==c :return b
  elif b==c :return a
  return a+b+c


# lucky_sum 

# In[4]:


def lucky_sum(a, b, c):
  if a!=13 and b!=13 and c!=13 :return a+b+c
  elif a==13 :return 0
  elif b==13 :return a
  elif c==13 :return a+b

