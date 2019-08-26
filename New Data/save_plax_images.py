import numpy as np
import os, fnmatch
from shutil import copyfile


fid=open('/media/ghazal/New Volume/plax_views.txt','r')
fid2=open('/media/ghazal/New Volume/plax_paths.txt','w')
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_file(pattern, path,folder):

    folder_found=0
    folder_path=[]
    for root, dirs, files in os.walk(path):
        # l=len(dirs)
        break
    for i in range(len(dirs)):
        path2=path+'/'+dirs[i]
        for root2, dirs2, files2 in os.walk(path2):
            if len(dirs2)!=0:
                k=path2+'/'+dirs2[0]+'/'+folder
                if os.path.isdir(k):
                    folder_found=1
                    folder_path.append(k)
            # for j in range(len(dirs2)):
            #     path3=path2+'/'+dirs2[j]
            #     for root3, dirs3, files3 in os.walk(path3):
            #         for k in range(len(dirs3)):
            #             if dirs3[k]==folder:
            #         cnt=cnt +1
            #         #
            # # else:
            #         print(cnt)
                    if os.path.isfile(k+pattern):
                        fid2.write(k+pattern)
                        fid2.write('\n')
                        return 1
                break

    print(folder_found,folder_path)
    print(pattern)
    print(folder)
    return 0




        # for name in files:
        #     if fnmatch.fnmatch(name, pattern):
        #         result.append(os.path.join(root, name))
cnt=0
for i in range(3200):

    arr=fid.readline()
    ind=find(arr,'/')
    folder=arr[ind[0]+1:ind[1]]
    if folder[-1]=='-':
        continue
    name=arr[ind[1]:-1]
    # folder=





    cnt+=find_file(name,'/media/ghazal/01D176301231DAE0/nas/Cardiac data_cleaned/cropped_data',folder)


    # def search_file(directory=None, file=None):
    #     assert os.path.isdir(directory)
    #     for cur_path, directories, files in os.walk(directory):
    #         if file in files:
    #             return os.path.join(directory, cur_path, file)
    #     return None
    print(cnt)
fid.close()
fid2.close()