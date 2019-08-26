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
# f2=open('/media/ghazal/New Volume/match2.txt',"w")
# f2=open('/media/ghazal/New Volume/dist_to_measures3.txt',"w")
# f3=open('/media/ghazal/New Volume/col_indcs3.txt',"w")

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
    # ind=find(name,'_')[-1]

    name=name[0:-10]
    # dists=np.zeros([len(arr)-2])
    # for i in range(len(dists)):
    #     dists[i]=arr[i+1]

    # print(dists)
    # f2.write(name)
    # f2.write(',')
    # f3.write(name)
    # f3.write(',')
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

    # mycursor.execute("SELECT * FROM exam where (HospID='00561967' OR Patient_ID='00561967') AND DateOfStudy=$date_str  ")
    # AND
    # DateOfStudy = % s
    # available=0
    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) ", (id, id))
    myresult = mycursor.fetchall()
    er=[]



    # partly_exist_flag=0
    ctt=0
    id_exist_flag=0
    date_match_flag=0
    date_null_flag=0
    null_cnt=0
    for x in myresult:
        # print(x)
        ctt=ctt+1
        col_num = 0
        id_exist_flag=1
        exist_flag = 0
        for y in x:
            # print(type(y))
            if type(y)==datetime.datetime and (col_num==92) and (y==None):
                # and (y!=None) and (col_num==):
                # print(col_num)
                # print('y:', y)
                date_null_flag=1

                # if (y.strftime('%Y-%m-%d')!=date_str):
                #     date_mismatch_cnt=date_mismatch_cnt+1
                #     # f2.write(name)
                #     # f2.write(',')
                #     # f2.write(date_str)
                #     # f2.write(',')
                #     # f2.write(y.strftime('%Y-%m-%d'))
                #     # f2.write('\n')
                #
                # else:
                #     date_match=date_match+1
                #     date_match_flag=1
                #     # f2.write(name)
                #     # f2.write(',')
                #     # f2.write(date_str)
                #     # f2.write(',')
                #     # f2.write(y.strftime('%Y-%m-%d'))
                #     # f2.write('\n')

                    # print(y)
                    # print(date_str)
                    #
                    # print(x)



            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
                # (col_num!=111)\
                # and (col_num!=137):
                # print('y: ', y)
                # print('type y:, ', type(y))
                # print('col_num: ', col_num)
                exist_flag=1



            # if y != 'None':
                # print(y)
                # for ii in range(len(dists)):
                #     d = np.absolute((dists[i]-float(y)))
                #     er.append(d)
                #     f2.write(str(d))
                #     f2.write(',')
                #     f3.write(str(col_num))
                #     f3.write(',')

            col_num = col_num + 1
        # print('exist flag:', exist_flag)
    if (id_exist_flag==0):
        available_count=available_count+1
    if (date_null_flag==1):
        null_cnt=null_cnt+1
    # if (tuple_count==0):
    #     noid_count=noid_count+1

    # else:
    #     print(name,id, date_str)
# print(available_count)
# print(noid_count)
# print(date_mismatch_cnt)
# print(date_match)
#         print(available_count)
#         print(id)
#         print(name)
print(null_cnt)

    # f2.write('\n')
    # f3.write('\n')
    # print(ind[-1])
    # print(len(arr[1:]))
f.close()
# f2.close()
# f3.close()