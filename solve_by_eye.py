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
f3=open('/media/ghazal/New Volume/ambiguous_plax.txt',"r")
field_names=[]
types_dict={0:"ivsd", 1:"lvd", 2:"lvs", 3:"pwd", 4:"root", 5:"lal", 6:"asc_aorta", 7:"lvot", 8:"LA"}
for i in range(453):
    arr = f.readline().split(',')
    field_names.append(arr)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def my_interface(name,mes):

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
    if len(myresult)==0:
        return
    d=[]
    b = []
    d.extend([None]*9)

    for x in myresult:
        col_num = 0
        for y in x:
            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):

                print('y: ', y)

                print('col_num: ', col_num)
                print(field_names[col_num])

                if col_num==167:
                    d[0]=np.abs(float(y)-mes)
                elif col_num==208:
                    d[1]=np.abs(float(y)-mes)
                elif col_num==213:
                    d[2]=np.abs(float(y) - mes)
                elif col_num==282:
                    d[3]=np.abs(float(y)-mes)
                elif col_num==296:
                    d[4]=np.abs(float(y) - mes)
                elif col_num==178:
                    d[5]=np.abs(float(y)-mes)
                elif col_num==61:
                    d[6]=np.abs(float(y)-mes)
                elif col_num==170:
                    d[8]=np.abs(float(y)-mes)
            col_num = col_num + 1
    return
name='014_1.2.840.113663.1500.1.374299194.3.14.20150812.121945.703'
frame='37'
f0 = open('/media/ghazal/New Volume/sorted_measurements_with_depth.txt', "r")
for i in range(109):
    arr = f0.readline().split(',')
    if name == arr[0][:] and arr[1]==frame:
        arr_len=len(arr)-2
        for j in range(2,len(arr)):
            mes=float(arr[j])*10
            found_lands=my_interface(name,mes)
f0.close()
f.close()
f3.close()
