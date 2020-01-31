import os
import numpy as np
import scipy.io as sio
LINE_NUM=394

f2=open('/media/ghazal/New Volume/LV3_combined_cm_dist_after_sort.txt',"w")

temp=[]
for filename in os.listdir('/media/ghazal/New Volume/Sorted_Heart/LV'):
    if filename.endswith('.jpg'):
        d_ind=filename.find('d')
        if d_ind!=-1:
            name=filename[0:d_ind-1]
        else:
            m_ind=filename.find('m')
            name = filename[0:m_ind-1]
        dash_ind=name.find('_')
        name=name[dash_ind+1:]
        print(filename)
        print(name)
        if (temp!=name):
            f = open('/media/ghazal/New Volume/combined_cm_dist_after_sort22.txt', "r")
            for i in range(LINE_NUM):

                arr = f.readline().split(',')
                if (arr[0][:]==name):
                    f2.write(name)
                    for j in range(len(arr)-1):
                        f2.write(',')
                        if(arr[j+1][-1]=='\n'):
                            arr[j+1]=arr[j+1][:-1]
                        f2.write(arr[j+1])
                    f2.write('\n')
                    f.close()
                    break
        temp=name
f2.close()
