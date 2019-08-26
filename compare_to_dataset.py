import os
import numpy as np
import mysql.connector
import pydicom
import scipy.io as sio

mydb = mysql.connector.connect(
  host="137.82.56.208",
  user="ghazal",
  passwd="ghazal",
  database="cardiac"
)

f=open('/media/ghazal/New Volume/cm_dist.txt',"r")
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
for i in range(394):
    arr=f.readline().split(',')
    name=arr[0][:]
    ind=find(name,'_')[-1]
    # print(name)
    name=name[0:ind-10]
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
        date=dcm_info['PatientID'][0]

    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    date_str = year + '-' + month + '-' + day
    mycursor = mydb.cursor()

    # mycursor.execute("SELECT * FROM exam where (HospID='00561967' OR Patient_ID='00561967') AND DateOfStudy=$date_str  ")
    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND DateOfStudy=%s", (id, id, date_str))
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


    # print(ind[-1])
    # print(len(arr[1:]))