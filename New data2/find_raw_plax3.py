import numpy as np
import os, fnmatch
from shutil import copyfile


fid=open('/media/ghazal/New Volume/plax_views2.txt','r')
fid2=open('/media/ghazal/New Volume/raw_plax_paths4.txt','w')
fid3=open('/media/ghazal/New Volume/raw_plax_paths4_not_found.txt','w')
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
def find_file_drive4(pattern, path,folder):
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
        for root2, dirs2, files2 in os.walk(path2):
            # if len(dirs2)!=0:
            break
        for j in range(len(dirs2)):
            path3=path2+'/'+dirs2[j]
            k=path3+'/'+folder
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


    #samira raw data drive 1:
    a=find_file(name,'/media/ghazal/01D176301231DAE0/nas/Cardiac data_cleaned/RawData/Drive1',folder)
    if a==0:
        # samira raw data drive 2:
        a = find_file(name, '/media/ghazal/01D176301231DAE0/nas/Cardiac data_cleaned/RawData/Drive2', folder)
    if a==0:
        # samira raw data drive 3:
        a = find_file(name, '/media/ghazal/01D176301231DAE0/nas/Cardiac data_cleaned/RawData/Drive3', folder)
    if a == 0:
        # samira raw data drive 4:
        a = find_file_drive4(name, '/media/ghazal/01D176301231DAE0/nas/Cardiac data_cleaned/RawData/Drive4', folder)
    if a==0:
        print(folder)
        fid3.write(folder)
        fid3.write(',')
        fid3.write(name)
        fid3.write('\n')
        print(name)
    cnt=cnt+a



    print(cnt)


fid.close()
fid2.close()
fid3.close()