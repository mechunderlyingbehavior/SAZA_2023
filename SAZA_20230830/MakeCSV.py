def makecsv(data_folder):
    from nptdms import TdmsFile
    import os, shutil
    import pandas as pd
    import numpy as np
    import re
    from GetFishTrace import GetFishTrace

    #data_folder = input("input the folder that contains .tdms file:")
    fullpath = 'C:/Users/ASMLabUser1/Desktop/SAZA_2018_1/%s' % data_folder


                                            ####################
                                            # TdmsToCSV function#
                                            ####################


    print('TDMS transformation to CSV: BEGIN ----')

    # get list of tdms files in folder
    tdmsfiles = []

    if os.path.exists(fullpath + '/RawData'):
        shutil.rmtree(fullpath + '/RawData')
    os.makedirs(fullpath + '/RawData', mode = 0o777,exist_ok=False)

    for File in os.listdir(fullpath):

        if File.endswith('.tdms'):
            filename,filetype = os.path.splitext(File)
            tdmsfiles.append(filename)
            print("filename:", filename)
            if os.path.exists(fullpath + '/RawData/'+filename):
                shutil.rmtree(fullpath + '/RawData'+filename)
            os.makedirs(fullpath+'/RawData/'+filename, mode = 0o777,exist_ok=False)

            print(fullpath+'/'+File)
            tdms_file = TdmsFile(fullpath+'/'+File)
            for group in tdms_file.groups():
                data = {}
                ch_name = []
                group_name = group.name
                #print("group:", group_name)
                for channel in group.channels():
                    channel_need = re.split('\W+', str(channel))[-2]
                    if channel_need in ['duration','type','Number','ms','time']:
                        continue
                    if channel_need == "Location":
                        channel_need = "Stimulus Location" 
                    ch_name.append(channel_need)
                    data[ch_name[-1]] = channel[:]

                df= pd.DataFrame(data)
                csv_path = fullpath +'/RawData/' + filename + '/' + group_name + '.csv'
                df.to_csv(csv_path, header=ch_name, float_format= '%.12f',index=False)



                                            ####################
                                            # LoadData function#
                                            ####################

    print('Load Data: BEGIN -----')
    _nsre = re.compile('([0-9]+)') 
    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower()
                for text in re.split(_nsre, s)]
    csvfiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(fullpath)
                for name in files
                if name == 'Tracker.csv']
    csvfiles.sort(key=natural_sort_key)
    iMax = len(csvfiles) 
    count = 1
    locationfiles = [os.path.join(root, name)
                 for root, dirs, files in os.walk(fullpath)
                 for name in files
                 if name == 'ExperimentInfo.csv']
    locationfiles.sort(key=natural_sort_key)
    if os.path.exists(fullpath+'/FishData'):
            shutil.rmtree(fullpath+'/FishData')
    os.makedirs(fullpath+ '/FishData')

    for i in range(0, iMax):
        # read csv file
        File=pd.read_csv(csvfiles[i])
        filename = re.search('\\\\(LOG.*?)\\\\', csvfiles[i])
        #print('filename type:',type(filename))
        # filename type: <class 're.Match'>
        Fish1 = GetFishTrace(File, 1)
        F1 = str(2*count-1)
        Fish2 = GetFishTrace(File, 2)
        F2 = str(2*count)
        #print('Fish {%s} = Fish 001: %s' % (F1, filename.group(1)))
        #print('Fish {%s} = Fish 002: %s' % (F2, filename.group(1)))
        # find location of stimulus
        locfile = pd.read_csv(locationfiles[i])
        stimLoc = locfile['Stimulus Location'][0]
        # Save fish numbers

        if i ==0:
            idfile = fullpath+'/FishData/Fish_number.txt'
            fid = open(idfile, 'w')
        else:
            idfile = fullpath + '/FishData/Fish_number.txt'
            fid = open(idfile, 'a')
        fid.write('%s' % ('Fish {'+F1+'} = Fish 001: '+filename.group(1)))
        fid.write('\n')
        fid.write('%s' % ('Fish {'+F2+'} = Fish 002: '+filename.group(1)))
        fid.write('\n')
        fid.close()

        # Save data for both fish
        df1 = pd.DataFrame(Fish1)
        df2 = pd.DataFrame(Fish2)
        df1.to_csv('%s/FishData/Fish {%s}_001_%s.csv' % (fullpath, F1, stimLoc), float_format= '%.12f',index=False)
        df2.to_csv('%s/FishData/Fish {%s}_002_%s.csv' % (fullpath, F2, stimLoc), float_format= '%.12f',index=False)
        count += 1        