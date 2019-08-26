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
# ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/007_1.2.840.113619.2.185.2838.1343722344.0.10.512.dcm')
# name='1.2.840.113619.2.98.1539.1285740630.0.1007.512'
mycursor = mydb.cursor()
for filename in os.listdir('/media/ghazal/01D176301231DAE0/GT mat files'):
    if filename.endswith('.mat'):
        file_counter=file_counter+1
        print(file_counter)
        print(filename)
        ind=filename.find('_')
        full_name=filename[:-10]
        name=filename[ind+1:-10]

        # dcm_filename = full_name + '.dcm'
        # mat_filename = full_name + '.mat'
        #
        # x_unit = 1
        # y_unit = 1
        # if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/' + dcm_filename):
        #     depth_dcm = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/' + dcm_filename)
        #     # dcminfo=depth_dcm.Se
        #     # ct1=ct1+1
        #     # print("hi")
        #     dd = depth_dcm.SequenceOfUltrasoundRegions
        #     if (dd[0].PhysicalUnitsXDirection == 4):
        #         x_unit = 0.1
        #
        #     if (dd[0].PhysicalUnitsYDirection == 4):
        #         y_unit = 0.1
        #     delta_x = dd[0].PhysicalDeltaX * x_unit
        #     delta_y = dd[0].PhysicalDeltaY * y_unit
        # else:
        #     depth_dcm = sio.loadmat('/media/ghazal/01D176301231DAE0/depth for blob/' + mat_filename)
        #     dcm_info = depth_dcm['Patient'][0, 0]['DicomInfo'][0, 0]['SequenceOfUltrasoundRegions'][0, 0]['Item_1'][
        #         0, 0]
        #     if (dcm_info['PhysicalUnitsXDirection'][0, 0] == 4):
        #         x_unit = 0.1
        #     if (dcm_info['PhysicalUnitsYDirection'][0, 0] == 4):
        #         Y_unit = 0.1
        #     delta_x = dcm_info['PhysicalDeltaX'][0, 0] * x_unit
        #     delta_y = dcm_info['PhysicalDeltaY'][0, 0] * y_unit


        params = {'value': name}
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
        for x in myresult2:
            frame_list.append(x[2])
            unique_frame_list=list(set(frame_list))

        for i in range(len(unique_frame_list)):

            # f.write(str(unique_frame_list[i]))

            mglist = []
            # sorted_frame_list=[]
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

                # for jj in range(2):

                # dist=np.sqrt((delta_y*(ps_y[0]-ps_y[1]))**2+(delta_x*(ps_x[0]-ps_x[1]))**2)
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



        # params = {'value1': InstanceIDK, 'value2':}




