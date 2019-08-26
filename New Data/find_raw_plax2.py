import numpy as np
import os, fnmatch
from shutil import copyfile


fid=open('/media/ghazal/New Volume/plax_views2.txt','r')
fid2=open('/media/ghazal/New Volume/raw_plax_paths4.txt','w')
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_file(pattern, path,folder):
    base_name=pattern[:-3]
    mat_name=base_name+'mat'
    dcm_name=base_name+'dcm'
    folder_found=0
    folder_path=[]
    for root, dirs, files in os.walk(path):
        # l=len(dirs)
        break
    for i in range(len(dirs)):
        path2=path+'/'+dirs[i]
        # for root2, dirs2, files2 in os.walk(path2):
        #     if len(dirs2)!=0:
        k=path2+'/'+folder
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

                # break
            if os.path.isfile(k+dcm_name):
                fid2.write(k+dcm_name)
                fid2.write('\n')
                return 1
            elif os.path.isfile(k + mat_name):
                fid2.write(k + mat_name)
                fid2.write('\n')
                return 1
                # break

    # print(folder_found,folder_path)
    # print(pattern)
    # print(folder)
    return 0
def find_file_in_plaxmat(pattern, path,folder):
    base_name=pattern[:-3]
    mat_name=base_name+'mat'
    dcm_name=base_name+'dcm'
    folder_found=0
    folder_path=[]
    # for root, dirs, files in os.walk(path):
    #     # l=len(dirs)
    #     break
    # for i in range(len(dirs)):
    #     path2=path+'/'+dirs[i]
        # for root2, dirs2, files2 in os.walk(path2):
        #     if len(dirs2)!=0:
    k=path+'/'+folder
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

                # break
        if os.path.isfile(k+dcm_name):
            fid2.write(k+dcm_name)
            fid2.write('\n')
            return 1
        elif os.path.isfile(k + mat_name):
            fid2.write(k + mat_name)
            fid2.write('\n')
            return 1
                # break

    # print(folder_found,folder_path)
    # print(pattern)
    # print(folder)
    return 0
def find_file_in_dys(pattern, path, folder):
    base_name = pattern[:-4]
    mat_name = base_name + '.mat'
    folder_path = []
    path2 = path +'/'+ 'MatAnon'
    k=path2+'/'+folder
    if os.path.isdir(k):
        folder_found = 1
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

            # break
        # if os.path.isfile(k + dcm_name):
        #     fid2.write(k + dcm_name)
        #     fid2.write('\n')
        #     return 1
        if os.path.isfile(k + mat_name):
            fid2.write(k + mat_name)
            fid2.write('\n')
            return 1
            # break

    # print(folder_found,folder_path)
    # print(pattern)
    # print(folder)
    return 0

def find_mat_file(pattern, path):
    base_name = pattern[:-4]
    mat_name = base_name + '.mat'
    dcm_name = base_name + '.dcm'
    folder_found = 0
    folder_path = []
    # for root, dirs, files in os.walk(path):
    #     # l=len(dirs)
    #     break
    # for i in range(len(dirs)):
    path2 = path + '/'
        # for root2, dirs2, files2 in os.walk(path2):
        #     if len(dirs2)!=0:
    k = path2 + base_name
    if os.path.isdir(k):
        folder_found = 1
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

            # break
        if os.path.isfile(k + dcm_name):
            fid2.write(k + dcm_name)
            fid2.write('\n')
            return 1
        elif os.path.isfile(k + mat_name):
            fid2.write(k + mat_name)
            fid2.write('\n')
            return 1
            # break

    # print(folder_found,folder_path)
    # print(pattern)
    # print(folder)
    return 0

    # for name in files:
    #     if fnmatch.fnmatch(name, pattern):
    #         result.append(os.path.join(root, name))





cnt=0
for i in range(371065):

    arr=fid.readline()
    ind=find(arr,'/')
    folder=arr[ind[-2]+1:ind[-1]]
    if folder[-1]=='-':
        continue
    name=arr[ind[-1]:-1]
    # folder=


    #parisa raw data echo_2:
    a=find_file(name,'/media/truecrypt7',folder)
    # parisa raw data echo:
    if a==0:
        a = find_file(name, '/media/truecrypt6', folder)

    #echo_2:
    if a==0:
        a=find_file(name,'/media/truecrypt3',folder)
    # echo_1:
    if a==0:
        a= find_file(name, '/media/truecrypt4', folder)

    # echo_1:
    if a==0:
        a= find_file(name, '/media/truecrypt2', folder)
    # Dys_batch1
    if a==0:
        a= find_file_in_dys(name, '/media/truecrypt5/DiastolicDysfunction_1731_2017.3.29', folder)

    # phase_detection_plax

    if a==0:
        a=find_mat_file(name,'/media/ghazal/01D176301231DAE0/cardiac/phase_detection_PLAX/PLAX_GT')
    #plax_files
    if a==0:
        a=find_file_in_plaxmat(name,'/media/ghazal/01D176301231DAE0/cardiac/7002463 (Echo)/PLAX_Files/Matfiles', folder)
    # nas
    if a==0:
        print(folder)
        print(name)
    cnt=cnt+a




    # def search_file(directory=None, file=None):
    #     assert os.path.isdir(directory)
    #     for cur_path, directories, files in os.walk(directory):
    #         if file in files:
    #             return os.path.join(directory, cur_path, file)
    #     return None
    print(cnt)


fid.close()
fid2.close()