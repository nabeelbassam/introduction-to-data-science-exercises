
# coding: utf-8

# string_times 

# In[1]:


def string_times(str, n):
  return str*n


# front_times 

# In[2]:


def front_times(str, n):
  return n*str[0:3]


# array123 

# In[4]:


def array123(nums):
  for x in range(len(nums)-2):
    if nums[x]==1 and nums[x+1]==2 and nums[x+2]==3 :
      return True
  return False


# array_front9 

# In[5]:


def array_front9(nums):
  for i in range(len(nums)):
    if i==4: break
    if nums[i]==9: return True
  return False  
   


# string_splosion 

# In[6]:


def string_splosion(str):
  string=""
  for n in range(len(str)):
    string =string+str[:n+1]
  return string

