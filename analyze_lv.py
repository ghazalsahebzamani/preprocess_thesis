
import os
import numpy as np
# import mysql.connector
# import pydicom
import scipy.io as sio
# import datetime
LINE_NUM=44
f2=open('/media/ghazal/New Volume/dist_to_measures6_10.txt',"r")
f3=open('/media/ghazal/New Volume/col_indcs6_10.txt',"r")
lv_ind_list=[]
for i in range(LINE_NUM):

    arr = f2.readline().split(',')
    arr2 = f3.readline().split(',')
    dists = np.zeros([len(arr)-2])
    for j in range(len(arr)-2): #to ignore the last '\n'
        dists[j]=arr[j+1]
    # print(arr2[np.argmin(dists)+1])
    # print(arr[np.argmin(dists)+1])
    lv_ind_list.append(arr2[np.argmin(dists)+1])
lv2=list(dict.fromkeys(lv_ind_list))
for i in range(len(lv2)):
    print(lv_ind_list.count(lv2[i]))
    print("col:", lv2[i])

f2.close()
f3.close()





