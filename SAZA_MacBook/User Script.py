#!/usr/bin/env python
# coding: utf-8

# # User Script

from MakeCSV import makecsv
from ROIData import ROIData
from Sparklines import Sparklines
from SaveTriggers import SaveTriggers
data_folder = input("input the folder that contains .tdms file:")
makecsv(data_folder)
ROIData(data_folder)
#Sparklines(data_folder)
#SaveTriggers(data_folder,0,1000,Bin_Lengths=['0-1000', '1000-2000', '2000-3000', '3000-5000','5000-8000','8000-11000', '11000-15000', '15000-20000'])




