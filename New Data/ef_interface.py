import numpy as np
import os
import mysql.connector
import scipy.io as sio
import pydicom
import datetime
mydb = mysql.connector.connect(
  host="137.82.56.208",
  user="ghazal",
  passwd="ghazal",
  database="cardiac"
)
f0=open('/home/ghazal/Downloads/edes.txt',"r")
f=open('/media/ghazal/New Volume/filemaker_fields.txt',"r")
f2=open('/home/ghazal/Downloads/edes_ef.txt',"w")
d=[]
d.extend([None]*3)
field_names=[]
for i in range(453):
    arr = f.readline().split(',')
    field_names.append(arr)
for i in range(14):
    name=f0.readline()[:-1]
    f2.write(name)
    f2.write(',')
    dcm_filename = name + '.dcm'
    mat_filename = name + '.mat'
    if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/' + dcm_filename):
        ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/' + dcm_filename)
        id = ds.PatientID
        date = ds.StudyDate
    else:
        ds = sio.loadmat('/media/ghazal/01D176301231DAE0/depth for blob/' + mat_filename)
        dcm_info = ds['Patient'][0, 0]['DicomInfo'][0, 0]
        id = dcm_info['PatientID'][0]
        date = dcm_info['StudyDate'][0]
    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    date_str = year + '-' + month + '-' + day
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND DateOfStudy=%s ", (id, id, date_str))
    myresult = mycursor.fetchall()
    # if len(myresult) == 0:
    #     return
    # d = []
    # b = []
    # d.extend([None] * 9)

    for x in myresult:
        col_num = 0
        for y in x:
            # if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
            if col_num==112 or col_num==113 or col_num==114:
                d[col_num-112]=y
                print('y: ', y)

                print('col_num: ', col_num)
                print(field_names[col_num])

                f
                # if col_num == 167:
                #     d[0] = np.abs(float(y) - mes)
                # elif col_num == 208:
                #     # f2.write('LVD')
                #
                #     d[1] = np.abs(float(y) - mes)
                # elif col_num == 213:
                #     # f2.write('LVS')
                #     d[2] = np.abs(float(y) - mes)
                # elif col_num == 282:
                #     # f2.write('PWD,')
                #     d[3] = np.abs(float(y) - mes)
                # elif col_num == 296:
                #     # f2.write('ROOT,')
                #     d[4] = np.abs(float(y) - mes)
                # elif col_num == 178:
                #     # f2.write('LA,')
                #     d[5] = np.abs(float(y) - mes)
                # elif col_num == 61:
                #     # f2.write('LA,')
                #     d[6] = np.abs(float(y) - mes)
                # elif col_num == 170:
                #     # f2.write('LA,')
                #     d[8] = np.abs(float(y) - mes)
                # elif col_num == 339:
                #     d[7] = np.abs(float(y) - mes)

            col_num = col_num + 1
        print("hi")
        for ii in range(3):
            if d[ii] is None:
                f2.write('-')
            else:
                f2.write(str(d[ii]))
            f2.write(',')
        f2.write('\n')
f2.close()