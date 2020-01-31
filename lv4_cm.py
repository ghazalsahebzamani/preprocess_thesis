import os
import scipy.io as sio
import numpy as np
import pydicom
f=open('/media/ghazal/New Volume/LV4_combined_cm_dist_after_sort.txt',"r")
cnt=0
for i in range(51):
    arr=f.readline().split(',')
    name=arr[0]
    dcm_filename = name + '.dcm'
    mat_filename = name + '.mat'
    x_unit = 1
    y_unit = 1
    if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/' + dcm_filename):
        depth_dcm = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/' + dcm_filename)
        dd = depth_dcm.SequenceOfUltrasoundRegions
        if (dd[0].PhysicalUnitsXDirection == 4):
            x_unit = 0.1

        if (dd[0].PhysicalUnitsYDirection == 4):
            y_unit = 0.1
        delta_x = dd[0].PhysicalDeltaX * x_unit
        delta_y = dd[0].PhysicalDeltaY * y_unit
    else:
        depth_dcm = sio.loadmat('/media/ghazal/01D176301231DAE0/depth for blob/' + mat_filename)
        dcm_info = depth_dcm['Patient'][0, 0]['DicomInfo'][0, 0]['SequenceOfUltrasoundRegions'][0, 0]['Item_1'][0, 0]
        if (dcm_info['PhysicalUnitsXDirection'][0, 0] == 4):
            x_unit = 0.1
        if (dcm_info['PhysicalUnitsYDirection'][0, 0] == 4):
            Y_unit = 0.1
        delta_x = dcm_info['PhysicalDeltaX'][0, 0] * x_unit
        delta_y = dcm_info['PhysicalDeltaY'][0, 0] * y_unit
    if delta_x!=delta_y:
        cnt=cnt+1
print(cnt)
