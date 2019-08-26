import numpy as np
import os
import mysql.connector
import scipy.io as sio
import pydicom
import datetime
mydb = mysql.connector.connect(
  host=" localhost",
  user="root",
  passwd="0017227755gG",
  database="echo"
)
counter=0
file_counter=0
WRITE_COUNT=1
f=open('/media/ghazal/New Volume/extracted_pairs_plax4.txt',"w+")
f2=open('/media/ghazal/01D176301231DAE0/nas/ghazal/raw_names4.txt',"r+")
# ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/007_1.2.840.113619.2.185.2838.1343722344.0.10.512.dcm')
# name='1.2.840.113619.2.98.1539.1285740630.0.1007.512'
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
mycursor = mydb.cursor()
for ii in range(...):
    arr=f2.readline()
    # ind = find(arr, '/')
    name = arr[:-1]
    dash_ind=np.amax(find(name,'_'))
    base_name=name[dash_ind+1:-4]

    print("study:", ii)

    params = {'value': base_name}
    # mycursor.execute("SELECT * FROM exam where (HospID='00561967' OR Patient_ID='00561967') AND DateOfStudy=$date_str  ")
    mycursor.execute("SELECT * FROM A_Instance where SOPInstanceUID=%(value)s", params)
    myresult = mycursor.fetchall()
    InstanceIDK=myresult[0][0]
    params = {'value': InstanceIDK}
    mycursor.execute("SELECT * FROM A_MeasGraphic where InstanceIdk=%(value)s", params)
    myresult2 = mycursor.fetchall()

    mycursor.execute("SELECT * FROM A_MeasPoint where InstanceIdk=%(value)s", params)
    myresult3 = mycursor.fetchall()
    frame_list=[]
    unique_frame_list=[]
    for x in myresult2:
        frame_list.append(x[2])
        unique_frame_list=list(set(frame_list))

    for i in range(len(unique_frame_list)):

        # f.write(str(unique_frame_list[i]))

        mglist = []
        # sorted_frame_list=[]
        for x in myresult2:
            if(x[2]==unique_frame_list[i]):
                mglist.append(x[1])
        for j in range(len(mglist)):
            f.write(name)
            f.write(",")
            f.write(str(unique_frame_list[i]))
            f.write(',')
            ps_x=[]
            ps_y=[]
            for xx in myresult3:
                if xx[1]==mglist[j]:

                    ps_x.append(xx[3])
                    ps_y.append(xx[4])

            # for jj in range(2):

            # dist=np.sqrt((delta_y*(ps_y[0]-ps_y[1]))**2+(delta_x*(ps_x[0]-ps_x[1]))**2)
            f.write(str(ps_x[0]))
            f.write(',')
            f.write(str(ps_x[1]))
            f.write(',')
            f.write(str(ps_y[0]))
            f.write(',')
            f.write(str(ps_y[1]))
            f.write('\n')
        counter=counter+1
        print(counter)
        # if(counter%WRITE_COUNT==0):
        #     f.close()
        #     f = open('/media/ghazal/New Volume/extracted_pairs_plax.txt', "a+")
f.close()
f2.close()