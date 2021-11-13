
# coding: utf-8

# has22 

# In[1]:


def has22(nums):
  for i in range(len(nums)-1):
    if nums[i]==2 and nums[i+1]==2 :return True
  return False



# count_evens 

# In[3]:


def count_evens(nums):
  counter=0
  for i in range(len(nums)):
   if nums[i]%2==0 :counter=counter+1
  return counter


# big_diff 

# In[4]:


def big_diff(nums):
  return max(nums)-min(nums)

