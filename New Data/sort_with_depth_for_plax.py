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
f=open('/media/ghazal/New Volume/plax_sorted_measurements_with_depth.txt',"w+")
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
mycursor = mydb.cursor()
path='/media/ghazal/01D176301231DAE0/nas/ghazal/data'
for filename in os.listdir(path):
    # if filename.endswith('.mat'):
    file_counter=file_counter+1
    print(file_counter)
    # print(filename)
    full_file_name=path+'/'+filename
    dash_ind=np.amax(find(filename,'_'))
    full_name=filename[:-4]
    base_name=filename[dash_ind+1:-4]
    mat_file=sio.loadmat(full_file_name)
    x_unit = 1
    y_unit = 1
    dcm_info = mat_file['Patient'][0, 0]['DicomInfo'][0, 0]['SequenceOfUltrasoundRegions'][0, 0]['Item_1'][
        0, 0]
    if (dcm_info['PhysicalUnitsXDirection'][0, 0] == 4):
        x_unit = 0.1
    if (dcm_info['PhysicalUnitsYDirection'][0, 0] == 4):
        Y_unit = 0.1
    delta_x = dcm_info['PhysicalDeltaX'][0, 0] * x_unit
    delta_y = dcm_info['PhysicalDeltaY'][0, 0] * y_unit

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
        f.write(full_name)
        f.write(",")
        f.write(str(unique_frame_list[i]))

        mglist = []
        for x in myresult2:
            if(x[2]==unique_frame_list[i]):
                mglist.append(x[1])
        for j in range(len(mglist)):
            ps_x=[]
            ps_y=[]
            for xx in myresult3:
                if xx[1]==mglist[j]:
                    ps_x.append(xx[3])
                    ps_y.append(xx[4])
            f.write(",")
            dist=np.sqrt((delta_y*(ps_y[0]-ps_y[1]))**2+(delta_x*(ps_x[0]-ps_x[1]))**2)
            f.write(str(dist))
        f.write('\n')
        counter=counter+1
        if(counter%WRITE_COUNT==0):
            f.close()
            f = open('/media/ghazal/New Volume/plax_sorted_measurements_with_depth.txt', "a+")
f.close()



        # params = {'value1': InstanceIDK, 'value2':}




