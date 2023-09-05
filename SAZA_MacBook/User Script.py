#!/usr/bin/env python
# coding: utf-8

# # User Script

# In[1]:


data_folder = input("input the folder that contains .tdms file:")
from MakeCSV import makecsv
from ROIData import ROIData
makecsv(data_folder)
ROIData(data_folder)


# In[ ]:




