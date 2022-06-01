#!/usr/bin/env python
# coding: utf-8

# In[3]:


# this is my first line of code for LSE

print('My name is Patrick')
print('The date is June 1st')


# In[15]:


# Write a program to analyse real estate dta

a = 45000
b = 23400
c = 67000
d = 34600
e = 12900

# Total Sales in December
sales = sum([a,b,c,d,e])
print('$', sales)

# Average sales Price
average_sales_price = sales / len([a, b, c, d, e])
print('$',round(average_sales_price))

# Property price C
comission_c = 6500
property_price_c = c - comission_c
print('$', property_price_c)


# In[ ]:




