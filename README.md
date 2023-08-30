# SAZA_2023_1
Done by Xinrui Li, @ 26-08-2023

Programming environment: Python 3.8.17;
numpy 1.24.3; matplotlib 3.7.1; pandas 1.5.3; nptdms 1.7.0 channel: conda forge

**Instructions of program files:**

**1.MakeCSV.py:** Firstly extract useful information from .tdms file and put in new .csv files, which are saved into `RawData`. Then infomation of each fish are extracted and saved in `FishData`. The log file 'Fish_number.txt'  is generated for recording fish number and the corresponding .tdms source.

**2.ROIData.py:** Foucsing on each ROI by pre/middle/post time, dynamic fish information are grouped and calculated, saving in `ROI.xlsx`. It includes 6 sheets which are separated by pre/middle/post time and left/right ROI region. 

**Parameters Interpretation:**

  1). Default pre/middle/post time were set in line 13 & 14 with `tmin` representing start time of each period and `tmax` representing end time of each period. For example the default setting indicates pre time is from 0 to 180, stimulus time is from 180 to 1260 and the post time is from 1260 to 1440.

If user wants to change the default time, please open this file and change the number inside.

![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/edc676a2-626d-4f87-8d28-a2a0d56ae700)
  
  2). Default sheet name of ROI.xlsx is set in line 34 as the image shows below. The dafault sheet names are based on stimulaus track of fish in left ROI and right ROI field.
  ![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/8832f423-2cb9-4e0b-83d4-f7b115db174c)


**Columns Interpretation:**

`TIn` and `TOut` record the time of fish entering and leaving ROI.

`MeanVIn` and `MeanVOut` record the mean velocity of fish entering and leaving ROI .

`StdVIn` and `StdVOut` record the standard deviation of velocity of fish entering and leaving ROI .

`BoundaryCrossings` indicates the number of times the fish entering and leaving the ROI area during detection.

`ENTRIES` = `BoundaryCrossings` / 2
`Mean T per entry` = `TIn`/`ENTRIES`
`sanity` = `TIn` + `TOut`
`% time in record` = `TIn` / `sanity` * 100 

**3. User Script.py:** This file is directly for user to run the program. More guideline please see `User Guideline.md`.

Before running the `User Script.py`, please make sure the following python modules have been installed:

- npTDMS 1.7.0 (channel: conda forge)
- Pandas 1.5.3
- Matplotlib 3.7.1
- NumPy 1.24.3


**User Guideline**

**1. Folder preparation**

    group your target .tdms file into one folder, name the folder as you want. Then copy the folder to this place:

   ![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/cc144e1b-222e-4787-be2f-999bd1b4f46f)

   ![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/34cf9de3-08af-4c67-a926-41d05b989b07)

    Please save your folder into 'SAZA_2018_1'.

**2. Set up program environment**

    1) Windows search bar input text 'anoconda prompt', and click to open the prompt.

![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/810030b0-f9f3-4ec9-a690-df7943d83f99)

    2) Enter text 'jupyter notebook' then click 'ENTER' button.

![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/7d8e9873-8ac8-41ab-9fd3-9a2352a0153a)

    3) Select folder and file :Desktop -> SAZA_2018_1 -> User Script.ipynb

![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/219c90bd-0178-46c0-8f46-33b44127719e)

![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/8b3cd697-df3d-4c7e-ad8a-a76edb1ac269)

![image](https://github.com/Ivy421/SAZA_2018/assets/57535126/31e21403-6df8-491e-b405-c2ed41adef7e)


