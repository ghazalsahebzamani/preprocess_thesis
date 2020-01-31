import os
import numpy as np
import mysql.connector
import pydicom
import scipy.io as sio
import datetime
mydb = mysql.connector.connect(
  host="137.82.56.208",
  user="ghazal",
  passwd="ghazal",
  database="cardiac"
)
LINE_NUM=51
f0=open('/media/ghazal/New Volume/sorted_measurements_with_depth.txt',"r")

f=open('/media/ghazal/New Volume/filemaker_fields.txt',"r")
f2=open('/media/ghazal/New Volume/landmark_types.txt',"w")
f3=open('/media/ghazal/New Volume/ambiguous_plax.txt',"w")
field_names=[]
types_dict={0:"ivsd", 1:"lvd", 2:"lvs", 3:"pwd", 4:"root", 5:"lal", 6:"asc_aorta", 7:"sinuses", 8:"LA"}
for i in range(453):
    arr = f.readline().split(',')
    field_names.append(arr)
def find_coords(name,frame,arr_len):
    fcoords = open('/media/ghazal/New Volume/extracted_pairs.txt', "r")
    found_len=0
    coord_list = []
    for j in range(1136):
        arr=fcoords.readline().split(',')
        if arr[0][:]==name and arr[1]==frame:
            found_len=found_len+1
            coord_list.append(float(arr[2]))


            if found_len==arr_len:
                fcoords.close()
                return coord_list

def solve_ivsd_pwd_ambig(coord_list,ind1,ind2):
    if coord_list[ind1]>coord_list[ind2]:
        return [0,3]
    else:
        return [3,0]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def my_interface(name,mes, found_lands,frame,arr_len):

    dcm_filename = name + '.dcm'
    mat_filename = name + '.mat'
    if os.path.isfile('/media/ghazal/01D176301231DAE0/depth for blob/'+ dcm_filename):
        ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/'+dcm_filename)
        id = ds.PatientID
        date = ds.StudyDate
    else:
        ds = sio.loadmat('/media/ghazal/01D176301231DAE0/depth for blob/' + mat_filename)
        dcm_info = ds['Patient'][0, 0]['DicomInfo'][0, 0]
        id=dcm_info['PatientID'][0]
        date=dcm_info['StudyDate'][0]

    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    date_str = year + '-' + month + '-' + day
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND DateOfStudy=%s ", (id, id, date_str))
    myresult = mycursor.fetchall()
    if len(myresult)==0:
        return
    d=[]
    b = []
    d.extend([None]*9)

    for x in myresult:
        col_num = 0
        for y in x:
            if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (type(y) != int):
                if col_num==167:
                    d[0]=np.abs(float(y)-mes)
                elif col_num==208:
                    d[1]=np.abs(float(y)-mes)
                elif col_num==213:
                    d[2]=np.abs(float(y) - mes)
                elif col_num==282:
                    d[3]=np.abs(float(y)-mes)
                elif col_num==296:
                    d[4]=np.abs(float(y) - mes)
                elif col_num==178:
                    d[5]=np.abs(float(y)-mes)
                elif col_num==61:
                    d[6]=np.abs(float(y)-mes)
                elif col_num==170:
                    d[8]=np.abs(float(y)-mes)
                elif col_num==339:
                    d[7]=np.abs(float(y)-mes)
            col_num = col_num + 1
    proposal_count = 0
    ambig_list = []
    for ii in range(len(d)):
        if d[ii] is not None:
            b.append(d[ii])
            if d[ii]<2.8:
                proposal_count=proposal_count+1
                ambig_list.append(ii)
    if proposal_count==0:
        print("none found for patient name:", name, "frame: ", frame)
        f3.write(name)
        f3.write(',')
        f3.write(frame)
        f3.write('\n')


    sorted_b=sorted(b)
    min_b=sorted_b[0]
    min_b2=sorted_b[1]

    margin=np.abs(min_b-min_b2)
    for ii in range(len(d)):
        if d[ii]==min_b:
            found_lands.append(ii)
            break
    if proposal_count>1 and margin<0.5:
        print("frame:",frame)
        if proposal_count>2:
            print('multi ambig list at:', ambig_list)
            print("name:",name)
            print("found :", found_lands)
        if 7 in ambig_list and 4 in ambig_list:
            if (0 in found_lands[:-1] or 3 in found_lands[:-1] or 1 in found_lands[:-1]):
                found_lands[-1]=7
                ambig_list.remove(4)
            else:
                print("one ambig error for patient: ", name)
                print("found:", found_lands)
                print("ambig:", ambig_list)
        if 1 in ambig_list and 8 in ambig_list:
            if 2 in found_lands[:-1]:
                found_lands[-1]=8
            elif 0 in found_lands or 3 in found_lands:
                found_lands[-1]=1
            else:
                print("one ambig error for patient: ", name)
                print("found:", found_lands)
                print("ambig:", ambig_list)
        elif 6 in ambig_list and 8 in ambig_list:
            if 2 in found_lands[:-1]:

                found_lands[-1] = 8
            elif 1 in found_lands:

                found_lands[-1] = 6
            else:
                print("one ambig error for patient: ", name)
                print("found:", found_lands)
                print("ambig:", ambig_list)
        elif 7 in ambig_list and 8 in ambig_list:
            if 2 in found_lands[:-1]:

                found_lands[-1] = 8
            elif 0 in found_lands[:-1] or 3 in found_lands[:-1] or 1 in found_lands[:-1]:
                found_lands[-1]=7
            else:
                print("one ambig error for patient: ", name)
                print("found:", found_lands)
                print("ambig:", ambig_list)

        elif 2 in ambig_list and 8 in ambig_list:
            if 2 in found_lands[:-1]:

                found_lands[-1] = 8
            else:
                print("one ambig error for patient: ", name)
                print("found:", found_lands)
                print("ambig:", ambig_list)
        elif len(set(found_lands))<len(found_lands):
            if 0 in ambig_list and 3 in ambig_list:
                if 0 in found_lands[:-1]:
                    indcs=find(found_lands,0)
                elif 3 in found_lands[:-1]:
                    indcs=find(found_lands,3)
                ind1=indcs[0]
                ind2=indcs[1]
                coord_list=find_coords(name,frame,arr_len)
                indcs=solve_ivsd_pwd_ambig(coord_list,ind1,ind2)
                found_lands[ind1]=indcs[0]
                found_lands[ind2] = indcs[1]
            elif arr_len>1:
                print("one ambig error for patient: ", name)
                print("found:",found_lands)
                print("ambig:", ambig_list)
        elif 0 not in ambig_list and 3 not in ambig_list:
            print("last case")
            print('ambig list',ambig_list)
            print('found lands',found_lands)
            print('name', name)
            print('frame,', frame)
    return found_lands
for i in range(109):
    found_lands=[]
    arr = f0.readline().split(',')
    name = arr[0][:]
    f2.write(name)
    f2.write(',')
    f2.write(arr[1])
    f2.write(',')
    arr_len=len(arr)-2
    frame=arr[1]
    for j in range(2,len(arr)):
        mes=float(arr[j])*10
        found_lands=my_interface(name,mes,found_lands,frame,arr_len)
    if found_lands is not None:
        for k in range(len(found_lands)):
            f2.write(types_dict[found_lands[k]])
            f2.write(',')
    f2.write('\n')
f.close()
f0.close()
f2.close()
f3.close()
