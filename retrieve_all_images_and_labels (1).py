import os.path

import numpy as np
from PIL import Image

nrows=128
ncols=128

path1=PATH_TO_YOUR_MOUNTED_NAS_DRIVE+ '/michael/img3/'
path2=PATH_TO_YOUR_MOUNTED_NAS_DRIVE+ '/michael/img4/'

NUM_OF_LINES_OF_TYPES_FILE=2589
def find_coords(name,frame,type,line_num):

    fcoords = open('.../extracted_pairs_all.txt', "r")

    coord_list = np.empty([5])
    for j in range(line_num):
        arr = fcoords.readline().split(',')
        if arr[0][:] == name and arr[1] == frame:
            for line_count in range(type):
                arr = fcoords.readline().split(',')
            x0=float(arr[2])
            x1=float(arr[3])
            y0=float(arr[4])
            y1=float(arr[5][:-1])
            coord_list[0]=x0
            coord_list[1]=y0
            coord_list[2]=x1
            coord_list[3]=y1
            return coord_list

def load_images(path1,path2,line_num,type):
    type_cnt=0
    names = []

    NUM_OF_LINES_OF_COORDS_FILE=4293
    f = open('.../plax_landmark_types_all.txt', "r")
    for i in range(line_num):
        arr=f.readline().split(',')
        whole_name=arr[0]
        name=arr[0][:-4]
        suffix=whole_name[-4:]
        frame=arr[1]
        found_type=0
        im_path=""
        if path.exists(path1+name+'_'+frame+suffix+'.jpg'):
            im_path=path1+name+'_'+frame+suffix+'.jpg'
        elif path.exists(path2+name+'_'+frame+suffix+'.jpg'):
            im_path=path2+name+'_'+frame+suffix+'.jpg'
        else:
            print("bug!")
            return
        for j in range(2,len(arr)):
            if arr[j]==type:
                coords=find_coords(whole_name,frame,j-2,NUM_OF_LINES_OF_COORDS_FILE)
                coords = np.expand_dims(coords, axis=0)
                found_type=1
                type_cnt+=1
                break
        if found_type==0:
            continue
        names.append(whole_name)


        im0= np.array(Image.open(im_path).convert('L'))
        x_orig=im0.shape[1]
        y_orig=im0.shape[0]
        coords[0][0]=ncols*coords[0][0]/x_orig
        coords[0][1]=nrows*coords[0][1]/y_orig
        coords[0][2]=ncols*coords[0][2]/x_orig
        coords[0][3] = nrows * coords[0][3] / y_orig
        coords[0][4]=np.sqrt((coords[0][2]-coords[0][0])**2+(coords[0][3]-coords[0][1])**2)
        im=np.array(Image.open(im_path).convert('L').resize((nrows, ncols)))
        im = np.reshape(im, (1, 128, 128, 1))
        if i==0:
            images=im
            all_coords=coords

        else:


            images=np.concatenate((images,im), axis=0)
            all_coords=np.concatenate((all_coords,coords),axis=0)
            print(type_cnt)
            print(len(names))
    return all_coords, images, names






#example of running the code, 'lvs' is a sample of the landmark type of ypur interest
labels,images, names = load_images(path1,path2,NUM_OF_LINES_OF_TYPES_FILE,'lvs')


