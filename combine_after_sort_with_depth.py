import os
import scipy.io as sio
import numpy as np
import pydicom
f=open('/media/ghazal/New Volume/combined_dist_after_sort_with_depth.txt',"w")
f2=open('/media/ghazal/New Volume/sorted_measurements_with_depth.txt',"r")
# ap2=[]
# ap4=[]
# for i in range(381):
#     [a,b]=f.readline().split(',')
#     # print(b)
#     # print(b[:-1])
#     ap2.append(a)
#     ap4.append(b[:-1])
# ap2=[]
# # ap4=[]
# for i in range(381):
#     [a,b]=f.readline().split(',')
#     # print(b)
#     # print(b[:-1])
#     ap2.append(a)
#     ap4.append(b[:-1])
temp=[]
ct=0
for i in range(648):
    line=f2.readline().split(',')


    # if len(line)==0:
    #     break
    patient_id = line[0][:]
    if temp!=patient_id:
        if ct>0:
            f.write('\n')
            print("hi")
        ct=1
        f.write(patient_id)
    temp=patient_id

    for ii in range(len(line)-2):
        # print(i)
        # print(ii)
        # print(line)
        f.write(',')
        if(line[ii+2][-1]=='\n'):
            line[ii+2]=line[ii+2][:-1]
        f.write(line[ii+2])

f.close()
f2.close()



















