#!/usr/bin/env python
# coding: utf-8

# In[2]:


var1 = 'US President Donald Trump will hold a second summit with North Korean leader Kim Jong Un in late February but will maintain economic sanctions on Pyongyang, the White House said on Friday after Trump met Pyongyang top nuclear negotiator.'
print(var1)


# In[3]:


var2 = 'The announcement came amid a diplomatic flurry in Washington surrounding the visit of Kim Yong Chol, a hardline former spy chief, and marked a sign of movement in a denuclearization effort that has stalled since a landmark meeting between Trump and the North Korean leader in Singapore on June 12'
print(var2)


# In[7]:


#Concatenate,Index,Slicing
print(var1 + var2)
print("Result =",var1[0])
print("Result =",var2[0:12])
print("Result =",var1[0:12])


# In[8]:


print("var in  ", "of" in var2)
print("var in  ", "of" not in var1)


# In[15]:


print("var in ", "or" in var2)


# In[12]:


#Capitalize,Lower,Upper
print( "capitalize() : ", var1.capitalize())#removes caps from the word
print( "lower : ", var2.lower())#prints the string in lower case
print("Upper : ",var2.upper())


# In[13]:


#Count
print( "Count of string(s) : ", var2.count("the"))


# In[14]:


#Length
print( "Length of a string: ", len(var2))


# In[16]:


#Title
print( "Title: ", var1.title())


# In[17]:


#Join
str1 = "_"
str2 = ("President","Donald","Trump")
print("Join",str1.join(str2))


# In[ ]:




