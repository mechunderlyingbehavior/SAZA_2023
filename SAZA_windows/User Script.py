#!/usr/bin/env python
# coding: utf-8

# # User Script

# In[5]:


from MakeCSV import makecsv
from  ROIData import ROIData_basic,ROIData_std, ROIData_180sec,ROIData_edit
from Sparklines import Sparklines
from SaveTriggers import SaveTriggers
data_folder = input("input the folder that contains .tdms file:")
#makecsv(data_folder)


# In[6]:


# for time section 0,180,1260,1440
ROIData_basic(data_folder)


# In[4]:


# for time section 0,180,720,1260,1440
ROIData_std(data_folder)


# In[7]:


# for time section every 3 mins
ROIData_180sec(data_folder)


# In[ ]:


# for editable time period
# ROIData_edit(data_folder,TMIN,TMAX)
ROIData_edit(data_folder,[0,100,200,300],[100,200,300,400])


# In[2]:


from MergeSheet import mergesheet
mergesheet()


# In[ ]:


#Sparklines(data_folder)


# In[ ]:


#SaveTriggers(data_folder,0,1000,Bin_Lengths=['0-1000', '1000-2000', '2000-3000', '3000-5000','5000-8000','8000-11000', '11000-15000', '15000-20000'])

