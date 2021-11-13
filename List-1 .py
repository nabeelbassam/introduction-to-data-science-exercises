
# coding: utf-8

# first_last6 

# In[1]:


def first_last6(nums):
  return nums[0]==6 or nums[len(nums)-1]==6


# make_pi 

# In[3]:


def make_pi():
  return [3,1,4]


# common_end 

# In[5]:


def common_end(a, b):
  return a[len(a)-1]==b[len(b)-1] or a[0]==b[0]


# sum3 

# In[6]:


def sum3(nums):
  return sum(nums)


# reverse3 

# In[7]:


def reverse3(nums):
  return nums[::-1]


# sum2 

# In[8]:


def sum2(nums):
  if len(nums)>=2 : return nums[0]+nums[1]
  elif len(nums)<2  : return sum(nums)
  else : return 0
  
  

