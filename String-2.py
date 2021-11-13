
# coding: utf-8

# count_code 

# In[1]:


def count_code(str):
  a=0
  if len(str)>=4:
    
    for i in range(len(str)):
      if str[i]=="c" :
        if i+1<len(str):
          
          if str[i+1]=="o":
            if i+3<len(str):
              if str[i+3]=="e":
                a=a+1
      
  return a


# double_char 

# In[2]:


def double_char(str):
  b=""
  a=str
  for i in range(len(str)):
    b = b+a[i] + str[i]
  return b


# count_hi 

# In[4]:


def count_hi(str):
  count=0
  a=len(str)
  for i in range(a-1):
    if str[i]=="h" and str[i+1]=="i" and i<a:
      count=count+1
  return count

