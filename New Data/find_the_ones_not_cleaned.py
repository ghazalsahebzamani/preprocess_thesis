import numpy as np
import os

# f=open('/media/ghazal/01D176301231DAE0/nas/ghazal/raw_names.txt',"w+")
f=open('/media/ghazal/01D176301231DAE0/nas/ghazal/raw_names3.txt',"w+")
# path='/media/ghazal/01D176301231DAE0/nas/ghazal/raw_data'
# path2='/media/ghazal/01D176301231DAE0/nas/ghazal/data'
# cnt=0
# not_cleaned_cnt=0
# for filename in os.listdir(path):
#     cnt=cnt+1
#     # new_filename = filename[:-4] + '.mat'
#     # if not os.path.isfile(path2+'/'+new_filename):
#     f.write(filename)
#     f.write('\n')
#         # not_cleaned_cnt +=1
#
#     print(cnt)
# # print('not cleaned:', not_cleaned_cnt)
# f.close()



# fid=open('/media/ghazal/New Volume/raw_plax_paths2.txt','r')
fid=open('/media/ghazal/New Volume/unique_raw_plax_paths3.txt','r')
# path="/media/ghazal/01D176301231DAE0/nas/ghazal/raw_data2/"

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
for i in range(13020):
    arr=fid.readline()

# for i in range(39):
#     print(i)
#     print(arr)
    # if i==1373:
    #     print("bug!")
    # arr = fid.readline()
    ind=find(arr,'/')
    name=arr[np.amax(ind)+1:-1]
    # file_name=path+name
    # copyfile(arr[:-1], file_name)
    f.write(name)
    f.write('\n')
f.close()
fid.close()
