def Sparklines(data_folder):
    #     Plot triggers
    #
    #     Plots how many times fish triggered odors
    #     (Python equivalent of Matlab function plot_triggers)
    #
    #     Returns:
    #        folder containing .jpg plots for each fish

    import os
    import shutil
    import re
    import matplotlib
    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np
    # import Tkinter, tkFileDialog

    data_folder = '%s/%s/FishData' %(os.getcwd(),data_folder)
    save_folder=os.path.dirname(data_folder)

    if os.path.exists(save_folder+'/SparkFigures'):
            shutil.rmtree(save_folder+'/SparkFigures')
    os.makedirs(save_folder+'/SparkFigures')

    _nsre = re.compile('([0-9]+)')
    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower()
                for text in re.split(_nsre, s)]
    csvfiles = []
    for File in os.listdir(data_folder):
        if File.startswith('Fish {') and File.endswith('.csv'):
            csvfiles.append(os.path.join(data_folder, File))
    csvfiles.sort(key=natural_sort_key)
    iMax = len(csvfiles)

    # every fish whose data we have
    for i in range(0, iMax):
        print('Fish..' + str(i+1))
        df=pd.read_csv(csvfiles[i])
        cnames = df.columns.tolist()
        time = df['T']
        if csvfiles[i][-8] == 'L':
            stimulus = cnames[1]
            control = cnames[2]
        else:
            stimulus = cnames[2]
            control = cnames[1]

        stim = np.asarray(df[stimulus].tolist())
        ctrl = np.asarray([ -x for x in df[control]])

        if stim[-1]!=0:
            stim = stim.append(0)
        if ctrl[-1]!=0:
            ctrl=ctrl.append(0)

        # plot triggers
        x_time = []
        x_time[:] = [x - min(time) for x in time]
        plt.figure(figsize=(26,12))
        plt.plot(x_time, stim, color='orange', label="stim")
        plt.fill_between(x_time, 0, stim, where=stim>0, color="orange")
        plt.plot(x_time, ctrl, color='blue', label="ctrl")
        plt.fill_between(x_time, 0, ctrl, where=ctrl<0, color="blue")
        plt.legend(loc='upper right',prop = {'size':20})
        # save figure
        filename = save_folder+'/SparkFigures/Sparklines_Fish'+str(i+1)+'.jpg'
        plt.savefig(filename, bbox_inches='tight')
        plt.show()
