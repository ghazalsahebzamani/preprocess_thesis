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
    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) ", (id, id))
    myresult = mycursor.fetchall()
    er=[]
    ctt=0
    id_exist_flag=0
    date_match_flag=0
    date_null_flag=0
    null_cnt=0
    for x in myresult:
        ctt=ctt+1
        col_num = 0
        id_exist_flag=1
        exist_flag = 0
        for y in x:
            if type(y)==datetime.datetime and (col_num==92) and (y==None):
                date_null_flag=1
            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
                exist_flag=1
            col_num = col_num + 1
    if (id_exist_flag==0):
        available_count=available_count+1
    if (date_null_flag==1):
        null_cnt=null_cnt+1
print(null_cnt)
f.close()
