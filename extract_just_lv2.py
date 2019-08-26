import os
import numpy as np
import scipy.io as sio
LINE_NUM=394

f2=open('/media/ghazal/New Volume/LV4_combined_cm_dist_after_sort.txt',"w")

# temp=[]
lv_names=[]
# lv_post_names=[]
for filename in os.listdir('/media/ghazal/New Volume/Sorted_Heart/LV'):
    if filename.endswith('.jpg'):
        d_ind = filename.find('d')

        if d_ind != -1:
            lv_name = filename[0:d_ind - 1]

        else:
            m_ind = filename.find('m')
            lv_name = filename[0:m_ind - 1]

        lv_names.append(lv_name)
        # lv_post_names.append(lv_post)

lv_names=list(dict.fromkeys(lv_names))
# lv_post_names=list(dict.fromkeys(lv_post_names))


for ii in range(len(lv_names)):
    full_name=lv_names[ii]
    dash_ind = filename.find('_')
    lv_post = full_name[dash_ind + 1:]
    f = open('/media/ghazal/New Volume/combined_cm_dist_after_sort22.txt', "r")
    # if ii==50:
    #     print("hi")
    for i in range(LINE_NUM):

        arr = f.readline().split(',')
        if (arr[0][:] == lv_post):
            f2.write(full_name)
            for j in range(len(arr) - 1):
                f2.write(',')
                if (arr[j + 1][-1] == '\n'):
                    arr[j + 1] = arr[j + 1][:-1]
                f2.write(arr[j + 1])
            f2.write('\n')
            f.close()
            break

f2.close()

# for filename in os.listdir('/media/ghazal/New Volume/Sorted_Heart/LV'):
#     if filename.endswith('.jpg'):
#         d_ind=filename.find('d')
#         if d_ind!=-1:
#             name=filename[0:d_ind-1]
#         else:
#             m_ind=filename.find('m')
#             name = filename[0:m_ind-1]
#         dash_ind=name.find('_')
#         name=name[dash_ind+1:]
#         print(filename)
#         print(name)
#         if (temp!=name):
#             f = open('/media/ghazal/New Volume/combined_cm_dist_after_sort22.txt', "r")
#             for i in range(LINE_NUM):
#
#                 arr = f.readline().split(',')
#                 if (arr[0][:]==name):
#                     f2.write(name)
#                     for j in range(len(arr)-1):
#                         f2.write(',')
#                         if(arr[j+1][-1]=='\n'):
#                             arr[j+1]=arr[j+1][:-1]
#                         f2.write(arr[j+1])
#                     f2.write('\n')
#                     f.close()
#                     break
#         temp=name
#
# # f.close()
# f2.close()
#
#     # name = arr[0][:]
#     # dcm_filename = name + '.dcm'
#     # mat_filename = name + '.mat'
#     #
#     # if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename):
#     #     ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/'+dcm_filename)
#     #     id = ds.PatientID
#     #     date = ds.StudyDate