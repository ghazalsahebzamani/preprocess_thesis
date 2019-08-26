import numpy as np
import mysql.connector
import pydicom
import scipy.io as sio
import datetime
f3=open('/media/ghazal/01D176301231DAE0/nas/ghazal/plax_landmark_types33_rgb.txt',"r")
f5=open('/media/ghazal/01D176301231DAE0/nas/ghazal/plax_landmark_types33_rgb2.txt',"w")
f4=open('/media/ghazal/01D176301231DAE0/nas/ghazal/doppler_rgb.txt',"r+")
dop_names=[]
cnt=0
for i in range(918):
    arr = f4.readline()
    dop_names.append(arr[:-5])

for i in range(1642):
    arr=f3.readline().split(',')
    name=arr[0]
    if name not in dop_names:
        cnt=cnt+1
        print(cnt)
        for j in range(len(arr)):
            if j!=len(arr)-1:
                f5.write(arr[j])
                f5.write(',')
            else:
                f5.write('\n')

        #     if j!=len(arr)-1:
        #         f5.write(arr[j])
        #         f5.write(',')
        #     else:
        #         f5.write(arr[j])
        # f5.write('\n')
f3.close()
f4.close()
f5.close()