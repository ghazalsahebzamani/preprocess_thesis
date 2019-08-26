import os
import numpy as np

f2=open('/media/ghazal/New Volume/LV2_combined_cm_dist_after_sort.txt',"w")
cnt=0
lv_names=[]
lv_post_names=[]
for filename in os.listdir('/media/ghazal/New Volume/Sorted_Heart/LV'):
    if filename.endswith('.jpg'):
        d_ind = filename.find('d')
        dash_ind = filename.find('_')
        if d_ind != -1:
            lv_name = filename[0:d_ind - 1]

        else:
            m_ind = filename.find('m')
            lv_name = filename[0:m_ind - 1]
        lv_post = lv_name[dash_ind + 1:]
        lv_names.append(lv_name)
        lv_post_names.append(lv_post)

lv_names=list(dict.fromkeys(lv_names))
lv_post_names=list(dict.fromkeys(lv_post_names))
# print(lv_names)
print(len(lv_names))
print(len(lv_post_names))
# for filename in os.listdir('/media/ghazal/01D176301231DAE0/GT mat files'):
#     lv_flag = 0
#     if filename.endswith('.mat'):
#         ind = filename.find('_')
#         full_name = filename[:-10]
#         post_name=filename[ind + 1:-10]
#         found_flag = 0
#
#
#
#         f = open('/media/ghazal/New Volume/LV_combined_cm_dist_after_sort.txt', "r")
#         for ii in range(57):
#             arr=f.readline().split(',')
#             name=arr[0][:]
#             if(post_name==name):
#                 # cnt = cnt + 1
#                 found_flag=1
#                 f2.write(full_name)
#                 # print(full_name)
#                 # print(name)
#                 # print(ii)
#                 # print(cnt)
#
#                 for j in range(len(arr)-1):
#                     f2.write(',')
#                     if(arr[j+1][-1]=='\n'):
#                         arr[j+1]=arr[j+1][:-1]
#                     f2.write(arr[j+1])
#                 f2.write('\n')
#                 f.close()
#                 break
#         if found_flag==0:
#             # print(post_name)
#             print(full_name)
#
# f2.close()
