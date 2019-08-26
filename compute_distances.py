import os
import scipy.io as sio
import numpy as np
import pydicom
f=open('/media/ghazal/New Volume/cm_dist.txt',"w")
# ap2=[]
# ap4=[]
# for i in range(381):
#     [a,b]=f.readline().split(',')
#     # print(b)
#     # print(b[:-1])
#     ap2.append(a)
#     ap4.append(b[:-1])
# ap2=[]
# # ap4=[]
# for i in range(381):
#     [a,b]=f.readline().split(',')
#     # print(b)
#     # print(b[:-1])
#     ap2.append(a)
#     ap4.append(b[:-1])
ct1=0
ct2=0
for filename in os.listdir('/media/ghazal/01D176301231DAE0/GT mat files'):
    # ct=ct+1
    if filename.endswith('.mat'):
        # print(filename)
        a=sio.loadmat('/media/ghazal/01D176301231DAE0/GT mat files/'+filename)
        # print("hi")
        dcm_filename = filename[:-10]+'.dcm'
        mat_filename = filename[:-10] + '.mat'

        x_unit = 1
        y_unit = 1
        if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename):
            depth_dcm=pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename)
            # dcminfo=depth_dcm.Se
            # ct1=ct1+1
            print("hi")
            dd = depth_dcm.SequenceOfUltrasoundRegions
            if (dd[0].PhysicalUnitsXDirection == 4):
                x_unit = 0.1

            if (dd[0].PhysicalUnitsYDirection == 4):
                y_unit = 0.1
            delta_x = dd[0].PhysicalDeltaX * x_unit
            delta_y = dd[0].PhysicalDeltaY * y_unit
        else:
            depth_dcm=sio.loadmat('/media/ghazal/01D176301231DAE0/depth for blob/'+ mat_filename)
            dcm_info=depth_dcm['Patient'][0,0]['DicomInfo'][0,0]['SequenceOfUltrasoundRegions'][0,0]['Item_1'][0,0]
            if (dcm_info['PhysicalUnitsXDirection'][0,0]==4):
                x_unit = 0.1
            if (dcm_info['PhysicalUnitsYDirection'][0,0]==4):
                Y_unit = 0.1
            delta_x = dcm_info['PhysicalDeltaX'][0,0] * x_unit
            delta_y = dcm_info['PhysicalDeltaY'][0,0] * y_unit
            print("hi2")
            # ct2=ct2+1





        for i in range(np.shape(a['Frames'])[1]):
            ar=np.argwhere(a['Segmentations'][i, :, :] > 0)
            y=ar[:,0]
            x=ar[:,1]
            l=len(y)
            dist=[]
            f.write(filename + '_' + str(a['Frames'][0,i]))
            f.write(',')
            for j in range(l):
                for k in range(l):
                    if j!=k:
                        d=np.sqrt(((y[j]-y[k])*delta_y)**2 + ((x[j]-x[k])*delta_x)**2)
                        dist.append(d)
            #\
            dist=list(dict.fromkeys(dist))
            for ii in range(len(dist)):

                f.write(str(d))
                f.write(',')
                f.write('\n')


            # print(dist)
    # if filename.endswith('.log'):
    #     with open(os.path.join('path/to/dir', filename)) as f:
    #         content = f.read()

f.close()