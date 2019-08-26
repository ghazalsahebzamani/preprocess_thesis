import numpy as np
import os, fnmatch
from shutil import copyfile
# fid=open('/media/ghazal/New Volume/raw_plax_paths2.txt','r')
fid=open('/media/ghazal/New Volume/new_unique_raw_plax_paths4.txt','r')
# path="/media/ghazal/01D176301231DAE0/nas/ghazal/raw_data2/"
path="/media/ghazal/01D176301231DAE0/nas/ghazal/raw_data4/"
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
for i in range(6446):
    arr=fid.readline()

# for i in range(39):
    ind=find(arr,'/')
    name=arr[np.amax(ind)+1:-1]
    file_name=path+name
    copyfile(arr[:-1], file_name)
    print(i)
