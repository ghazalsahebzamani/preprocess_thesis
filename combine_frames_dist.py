import os
import scipy.io as sio
import numpy as np
import pydicom
f=open('/media/ghazal/New Volume/combined_cm_dist.txt',"w")
ct1=0
ct2=0
for filename in os.listdir('/media/ghazal/01D176301231DAE0/GT mat files'):
    if filename.endswith('.mat'):
        a=sio.loadmat('/media/ghazal/01D176301231DAE0/GT mat files/'+filename)
        dcm_filename = filename[:-10]+'.dcm'
        mat_filename = filename[:-10] + '.mat'
        x_unit = 1
        y_unit = 1
        f.write(filename)
        f.write(',')
        if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename):
            depth_dcm=pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename)
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
        for i in range(np.shape(a['Frames'])[1]):
            ar=np.argwhere(a['Segmentations'][i, :, :] > 0)
            y=ar[:,0]
            x=ar[:,1]
            l=len(y)
            dist=[]

            for j in range(l):
                for k in range(l):
                    if j!=k:
                        d=np.sqrt(((y[j]-y[k])*delta_y)**2 + ((x[j]-x[k])*delta_x)**2)
                        dist.append(d)
            dist = list(dict.fromkeys(dist))
            for ii in range(len(dist)):
                f.write(str(d))
                f.write(',')
        f.write('\n')

f.close()
