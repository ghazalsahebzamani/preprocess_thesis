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
LINE_NUM=51
f=open('/media/ghazal/New Volume/filemaker_fields.txt',"r")
field_names=[]
for i in range(453):
    arr = f.readline().split(',')
    field_names.append(arr)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def my_interface(name):
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
    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND DateOfStudy=%s ", (id, id, date_str))
    myresult = mycursor.fetchall()
    for x in myresult:
        col_num = 0
        for y in x:
            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
                print('y: ', y)
                print('col_num: ', col_num)
                print(field_names[col_num])
            col_num = col_num + 1
my_interface('007_1.2.840.113619.2.185.2838.1343722344.0.10.512')
