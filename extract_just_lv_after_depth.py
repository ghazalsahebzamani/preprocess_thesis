import os
import numpy as np
import scipy.io as sio
LINE_NUM=394

f2=open('/media/ghazal/New Volume/LV4_combined_cm_dist_after_sort_after_depth.txt',"w")

lv_names=[]
for filename in os.listdir('/media/ghazal/New Volume/Sorted_Heart/LV'):
    if filename.endswith('.jpg'):
        d_ind = filename.find('d')

        if d_ind != -1:
            lv_name = filename[0:d_ind - 1]

        else:
            m_ind = filename.find('m')
            lv_name = filename[0:m_ind - 1]

        lv_names.append(lv_name)

lv_names=list(dict.fromkeys(lv_names))
for ii in range(len(lv_names)):
    full_name=lv_names[ii]
    f = open('/media/ghazal/New Volume/combined_dist_after_sort_with_depth.txt', "r")
    for i in range(LINE_NUM):

        arr = f.readline().split(',')
        if (arr[0][:] == full_name):
            f2.write(full_name)
            for j in range(len(arr) - 1):
                f2.write(',')
                if (arr[j + 1][-1] == '\n'):
                    arr[j + 1] = arr[j + 1][:-1]
                f2.write(arr[j + 1])
            f2.write('\n')
            f.close()
            break

f2.close()
