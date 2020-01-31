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
f=open('/media/ghazal/New Volume/extracted_pairs.txt',"w+")
mycursor = mydb.cursor()
for filename in os.listdir('/media/ghazal/01D176301231DAE0/GT mat files'):
    if filename.endswith('.mat'):
        file_counter=file_counter+1
        print(file_counter)
        print(filename)
        ind=filename.find('_')
        full_name=filename[:-10]
        name=filename[ind+1:-10]
        params = {'value': name}
        mycursor.execute("SELECT * FROM A_Instance where SOPInstanceUID=%(value)s", params)
        myresult = mycursor.fetchall()
        InstanceIDK=myresult[0][0]
        params = {'value': InstanceIDK}
        mycursor.execute("SELECT * FROM A_MeasGraphic where InstanceIdk=%(value)s", params)
        myresult2 = mycursor.fetchall()

        mycursor.execute("SELECT * FROM A_MeasPoint where InstanceIdk=%(value)s", params)
        myresult3 = mycursor.fetchall()
        frame_list=[]
        for x in myresult2:
            frame_list.append(x[2])
            unique_frame_list=list(set(frame_list))

        for i in range(len(unique_frame_list)):

            mglist = []
            for x in myresult2:
                if(x[2]==unique_frame_list[i]):
                    mglist.append(x[1])
            for j in range(len(mglist)):
                f.write(full_name)
                f.write(",")
                f.write(str(unique_frame_list[i]))
                f.write(',')
                ps_x=[]
                ps_y=[]
                for xx in myresult3:
                    if xx[1]==mglist[j]:

                        ps_x.append(xx[3])
                        ps_y.append(xx[4])
                f.write(str(ps_x[0]))
                f.write(',')
                f.write(str(ps_x[1]))
                f.write(',')
                f.write(str(ps_y[0]))
                f.write(',')
                f.write(str(ps_y[1]))
                f.write('\n')
            counter=counter+1
            if(counter%WRITE_COUNT==0):
                f.close()
                f = open('/media/ghazal/New Volume/extracted_pairs.txt', "a+")
f.close()





