import pydicom
import scipy.io as sio

f=open('/media/ghazal/01D176301231DAE0/nas/ghazal/raw_names3.txt',"r+")
f2=open('/media/ghazal/01D176301231DAE0/nas/ghazal/doppler_names3.txt',"w+")
path='/media/ghazal/01D176301231DAE0/nas/ghazal/raw_data3/'
cnt=0
for i in range(13020):
    print(i,cnt)
    arr=f.readline()
    # ind = find(arr, '/')
    name = arr[:-1]
    if name[-4:] == '.dcm':
        depth_dcm = pydicom.dcmread(path + name)
        dd = depth_dcm.SequenceOfUltrasoundRegions
        if dd[0].RegionDataType==2:
            cnt+=1
            f2.write(name)
            f2.write('\n')
        elif dd[0].RegionDataType!=1:
            print("bug!!")
    elif name[-4:] == '.mat':

        depth_dcm = sio.loadmat(path + name)
        dcm_info = depth_dcm['Patient'][0, 0]['DicomInfo'][0, 0]['SequenceOfUltrasoundRegions'][0, 0]['Item_1'][
            0, 0]
        if (dcm_info['RegionDataType'][0, 0] == 2 or dcm_info['RegionFlags'][0, 0]==2)
            cnt += 1
            f2.write(name)
            f2.write('\n')
        elif (dcm_info['RegionDataType'][0, 0] != 1):
            print("bug!!")

f.close()
f2.close()
