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

#
f=open('/media/ghazal/New Volume/filemaker_fields.txt',"r")
# f2=open('/media/ghazal/New Volume/landmark_types.txt',"w")
f3=open('/media/ghazal/New Volume/ambiguous_plax.txt',"r")
field_names=[]
types_dict={0:"ivsd", 1:"lvd", 2:"lvs", 3:"pwd", 4:"root", 5:"lal", 6:"asc_aorta", 7:"lvot", 8:"LA"}
for i in range(453):
    arr = f.readline().split(',')
    field_names.append(arr)
# def find_coords(name,frame,arr_len):
#     fcoords = open('/media/ghazal/New Volume/extracted_pairs.txt', "r")
#     found_len=0
#     coord_list = []
#     for j in range(1136):
#         arr=fcoords.readline().split(',')
#         if arr[0][:]==name and arr[1]==frame:
#             found_len=found_len+1
#             coord_list.append(float(arr[2]))
#
#
#             if found_len==arr_len:
#                 fcoords.close()
#                 return coord_list
#
# def solve_ivsd_pwd_ambig(coord_list,ind1,ind2):
#     if coord_list[ind1]>coord_list[ind2]:
#         return [0,3]
#     else:
#         return [3,0]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def my_interface(name,mes):

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

                print('y: ', y)

                print('col_num: ', col_num)
                print(field_names[col_num])

                if col_num==167:
                    d[0]=np.abs(float(y)-mes)
                elif col_num==208:
                    # f2.write('LVD')

                    d[1]=np.abs(float(y)-mes)
                elif col_num==213:
                    # f2.write('LVS')
                    d[2]=np.abs(float(y) - mes)
                elif col_num==282:
                    # f2.write('PWD,')
                    d[3]=np.abs(float(y)-mes)
                elif col_num==296:
                    # f2.write('ROOT,')
                    d[4]=np.abs(float(y) - mes)
                elif col_num==178:
                    # f2.write('LA,')
                    d[5]=np.abs(float(y)-mes)
                elif col_num==61:
                    # f2.write('LA,')
                    d[6]=np.abs(float(y)-mes)
                elif col_num==170:
                    # f2.write('LA,')
                    d[8]=np.abs(float(y)-mes)

            col_num = col_num + 1
    # proposal_count = 0
    # ambig_list = []
    # for ii in range(len(d)):
    #
    #     if d[ii] is not None:
    #         b.append(d[ii])
    #         if d[ii]<0.5:
    #             proposal_count=proposal_count+1
    #             ambig_list.append(ii)
    # if proposal_count==0:
    #     print("none found for patient name:", name, "frame: ", frame)
    #     f3.write(name)
    #     f3.write(',')
    #     f3.write(frame)
    #     f3.write('\n')
    #
    #
    #
    # min_b=np.amin(np.asarray(b))
    # for ii in range(len(d)):
    #     if d[ii]==min_b:
    #         found_lands.append(ii)
    #         # f2.write(types_dict[ii])
    #         # f2.write(',')
    #         break
    # if proposal_count>1:
    #     print("frame:",frame)
    #
    #     if ambig_list == [1, 8]:
    #         lvs_ind = find(found_lands, 2)
    #         if len(lvs_ind) > 0:
    #             found_lands[-1] = 8
    #         else:
    #             print("one ambig error for patient: ", name)
    #             print("found:", found_lands)
    #             print("ambig:", ambig_list)
    #     elif ambig_list == [6, 8]:
    #         lvs_ind = find(found_lands, 2)
    #         lvd_ind = find(found_lands, 1)
    #         if len(lvs_ind) > 0:
    #
    #             found_lands[-1] = 8
    #         elif len(lvd_ind) > 0:
    #
    #             found_lands[-1] = 6
    #         else:
    #             print("one ambig error for patient: ", name)
    #             print("found:", found_lands)
    #             print("ambig:", ambig_list)
    #     elif ambig_list == [2, 8]:
    #         lvs_ind = find(found_lands, 2)
    #         # lvd_ind = find(found_lands, 1)
    #         if len(lvs_ind) > 0:
    #
    #             found_lands[-1] = 8
    #         else:
    #             print("one ambig error for patient: ", name)
    #             print("found:", found_lands)
    #             print("ambig:", ambig_list)
    #         # elif len(lvd_ind) > 0:
    #         #
    #         #     found_lands[-1] = 6
    #
    #
    #
    #     elif len(set(found_lands))<len(found_lands):
    #         # print('multi error for patient: ', name)
    #         # for ii in range(len(d)):
    #         #     if d[ii] is not None and d[ii]<1.5:
    #         #         # print(types_dict[ii])
    #         #         ambig_list.append(ii)
    #         if ambig_list==[0,3]:
    #             indcs=find(found_lands,0)
    #             ind1=indcs[0]
    #             ind2=indcs[1]
    #             coord_list=find_coords(name,frame,arr_len)
    #             indcs=solve_ivsd_pwd_ambig(coord_list,ind1,ind2)
    #             found_lands[ind1]=indcs[0]
    #             found_lands[ind2] = indcs[1]
    #             #solve la ambig
    #         else:
    #             print('multi error for patient: ', name)
    #             print(ambig_list)
    #
    #
    #     else:
    #         print("one ambig error for patient: ", name)
    #         print("found:",found_lands)
    #         print("ambig:", ambig_list)
    #
    # # if arr_len==1:
    # #     print("possible lvot!!!")
    # #     print(name)
    # #     print(d)
    # #     print(found_lands)
    #
    #
    #     # for x in myresult:
    #     #     col_num = 0
    #     #     for y in x:
    #     #         if (y != None) and (type(y) != str) and (y != 1) and type(y) != datetime.datetime and (
    #     #                 type(y) != int):
    #     #             #
    #     #             print('y: ', y)
    #     #
    #     #             print('col_num: ', col_num)
    #     #             print(field_names[col_num])
    #     #
    #     #             # if col_num == 167:
    #     #             #     d[0] = np.abs(float(y) - mes)
    #     #             # elif col_num == 208:
    #     #             #     # f2.write('LVD')
    #     #             #
    #     #             #     d[1] = np.abs(float(y) - mes)
    #     #             # elif col_num == 213:
    #     #             #     # f2.write('LVS')
    #     #             #     d[2] = np.abs(float(y) - mes)
    #     #             # elif col_num == 282:
    #     #             #     # f2.write('PWD,')
    #     #             #     d[3] = np.abs(float(y) - mes)
    #     #             # elif col_num == 296:
    #     #             #     # f2.write('ROOT,')
    #     #             #     d[4] = np.abs(float(y) - mes)
    #     #             # elif col_num == 178:
    #     #             #     # f2.write('LA,')
    #     #             #     d[5] = np.abs(float(y) - mes)
    #     #             # elif col_num == 61:
    #     #             #     # f2.write('LA,')
    #     #             #     d[6] = np.abs(float(y) - mes)
    #     #             # elif col_num == 170:
    #     #             #     # f2.write('LA,')
    #     #             #     d[8] = np.abs(float(y) - mes)
    #     #             # else:
    #     #             #
    #     #             #     print('y: ', y)
    #     #             #
    #     #             #     # print('col_num: ', col_num)
    #     #             #     print(field_names[col_num])
    #     #
    #     #         col_num = col_num + 1
    #
    # return found_lands
    #
    return

# for j in range(23):
#     arr0=f3.readline().split(',')
#     name=arr0[0][:]
#     frame=arr0[1][:-1]
name='014_1.2.840.113663.1500.1.374299194.3.14.20150812.121945.703'
frame='37'
f0 = open('/media/ghazal/New Volume/sorted_measurements_with_depth.txt', "r")
for i in range(109):

    arr = f0.readline().split(',')
    if name == arr[0][:] and arr[1]==frame:
        arr_len=len(arr)-2
        for j in range(2,len(arr)):
            mes=float(arr[j])*10
            found_lands=my_interface(name,mes)
f0.close()




#
# for j in range(23):
#     arr0=f3.readline().split(',')
#     name=arr0[0][:]
#     frame=arr0[1][:-1]
#
#
#
#     # 002_1.2
#     # .840
#     # .113619
#     # .2
#     # .98
#     # .8523
#     # .1391756277
#     # .0
#     # .39424
#     # .512
#
#     # 001_1.2
#     # .840
#     # .113663
#     # .1500
#     # .1
#     # .370175126
#     # .3
#     # .1
#     # .20130313
#     # .81222
#     # .875
#
#
#     #root
#     # 002_1.2
#     # .840
#     # .113663
#     # .1500
#     # .1
#     # .184044681
#     # .3
#     # .3
#     # .20121201
#     # .101026
#     # .312
#
#     # 002_1.2
#     # .840
#     # .113663
#     # .1500
#     # .1
#     # .184052985
#     # .3
#     # .2
#     # .20120731
#     # .162301
#     # .78
#
#     # 001_1.2
#     # .840
#     # .113663
#     # .1500
#     # .1
#     # .370175126
#     # .3
#     # .1
#     # .20151110
#     # .153753
#     # .359
#
#
#     #pwd?!
#     # 001_1.2
#     # .840
#     # .113663
#     # .1500
#     # .1
#     # .370175126
#     # .3
#     # .1
#     # .20130528
#     # .121107
#     # .687
#
#     #asc aorta?!
#     # 014_1.2
#     # .840
#     # .113663
#     # .1500
#     # .1
#     # .367412876
#     # .3
#     # .15
#     # .20140604
#     # .154742
#     # .406
#     # if name=='001_1.2.840.113619.2.297.50330.1391695696.0.4.512':
#     #     print("bug!")
#     # elif name=='007_1.2.840.113663.1500.1.184044681.3.7.20120925.93249.687':
#     #     print("bug!")
#
#     f0 = open('/media/ghazal/New Volume/sorted_measurements_with_depth.txt', "r")
#     for i in range(109):
#
#         arr = f0.readline().split(',')
#         if name == arr[0][:] and arr[1]==frame:
#             arr_len=len(arr)-2
#             for j in range(2,len(arr)):
#                 mes=float(arr[j])*10
#                 found_lands=my_interface(name,mes)
#     f0.close()

f.close()

# f2.close()
f3.close()