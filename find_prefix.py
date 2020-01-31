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
print(len(lv_names))
print(len(lv_post_names))
