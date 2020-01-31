import os
import numpy as np
import mysql.connector
import pydicom
import scipy.io as sio
import datetime
mydb = mysql.connector.connect(
  host="137.82.56.208",
  user="ghazal",
  passwd="ghazal",
  database="cardiac"
)
f=open('/media/ghazal/New Volume/combined_cm_dist.txt',"r")
f2=open('/media/ghazal/New Volume/weird_stuff.txt',"w")
f3=open('/media/ghazal/New Volume/match.txt',"w")

available_count=0
no_date_count=0
date_mismatch_cnt=0
noid_count=0
date_match=0
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
for i in range(394):
    arr=f.readline().split(',')
    name=arr[0][:]
    name=name[0:-10]
    dcm_filename = name + '.dcm'
    mat_filename = name + '.mat'
    if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename):
        ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/'+dcm_filename)
        id = ds.PatientID
        date = ds.StudyDate
    else:
        ds = sio.loadmat('/media/ghazal/01D176301231DAE0/depth for blob/' + mat_filename)
        dcm_info = ds['Patient'][0, 0]['DicomInfo'][0, 0]
        id=dcm_info['PatientID'][0]
        date=dcm_info['StudyDate'][0]

    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    date_str = year + '-' + month + '-' + day
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND (DateOfStudy = %s)", (id, id, date_str))
    myresult = mycursor.fetchall()
    er=[]
    col_num=0
    exist_flag = 0
    for x in myresult:
        for y in x:
            if type(y)==datetime.datetime and (col_num==92):
                if (y.strftime('%Y-%m-%d')!=date_str):
                    date_mismatch_cnt=date_mismatch_cnt+1
                    f2.write(name)
                    f2.write(',')
                    f2.write(date_str)
                    f2.write(y.strftime('%Y-%m-%d'))
                    f2.write('\n')

                else:
                    date_match=date_match+1
                    f3.write(name)
                    f3.write(',')
                    f3.write(date_str)
                    f3.write(y.strftime('%Y-%m-%d'))
                    f3.write('\n')
            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
                exist_flag=1
            col_num = col_num + 1
    if (exist_flag):
        available_count=available_count+1
print(date_mismatch_cnt)
print(date_match)
print(available_count)
f.close()
f2.close()
f3.close()
