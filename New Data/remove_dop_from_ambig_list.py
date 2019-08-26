import numpy as np
import mysql.connector
import pydicom
import scipy.io as sio
import datetime
f3=open('/media/ghazal/01D176301231DAE0/nas/ghazal/ambiguous_plax33_rgb.txt',"r")
f5=open('/media/ghazal/01D176301231DAE0/nas/ghazal/ambiguous_plax33_rgb2.txt',"w")
f4=open('/media/ghazal/01D176301231DAE0/nas/ghazal/doppler_rgb.txt',"r+")
dop_names=[]
cnt=0
for i in range(918):
    arr = f4.readline()
    dop_names.append(arr[:-5])

for i in range(325):
    arr=f3.readline().split(',')
    name=arr[0]
    frame=arr[1][:-1]
    if name not in dop_names:
        cnt=cnt+1
        print(cnt)
        f5.write(name)
        f5.write(',')
        f5.write(frame)
        f5.write('\n')

f3.close()
f4.close()
f5.close()