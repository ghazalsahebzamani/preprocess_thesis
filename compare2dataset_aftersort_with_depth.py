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
f=open('/media/ghazal/New Volume/LV4_combined_cm_dist_after_sort.txt',"r")
f2=open('/media/ghazal/New Volume/dist_to_measures5.txt',"w")
f3=open('/media/ghazal/New Volume/col_indcs5.txt',"w")
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
for i in range(LINE_NUM):
    arr=f.readline().split(',')
    name=arr[0][:]
    # ind=find(name,'_')[-1]

    # name=name[0:-10]
    dists=np.zeros([len(arr)-1])
    for ii in range(len(dists)):
        dists[ii]=arr[ii+1]
    # dists[-1]=dists[-1][:-1]

    # print(dists)
    # print(arr)
    dcm_filename = name + '.dcm'
    mat_filename = name + '.mat'
    # print(i)
    # print(name)
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

    # mycursor.execute("SELECT * FROM exam where (HospID='00561967' OR Patient_ID='00561967') AND DateOfStudy=$date_str  ")
    # AND
    # DateOfStudy = % s
    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND DateOfStudy=%s ", (id, id, date_str))
    myresult = mycursor.fetchall()
    er=[]

    for x in myresult:
        # print(x)
        col_num = 0
        f2.write(name)
        f2.write(',')
        f3.write(name)
        f3.write(',')
        for y in x:
            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
                # (col_num!=111)\
                # and (col_num!=137):
                # print('y: ', y)
                # print('type y:, ', type(y))
                # print('col_num: ', col_num)


            # if y != 'None':
                # print(y)
                for ii in range(len(dists)):
                    d = np.absolute((dists[ii]-float(y)))
                    er.append(d)
                    f2.write(str(d))
                    f2.write(',')
                    f3.write(str(col_num))
                    f3.write(',')

            col_num = col_num + 1

        f2.write('\n')
        f3.write('\n')
    # print(ind[-1])
    # print(len(arr[1:]))
f.close()
f2.close()
f3.close()