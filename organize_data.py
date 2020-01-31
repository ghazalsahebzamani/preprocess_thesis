f=open('/media/ghazal/New Volume/landmark_types.txt',"r")

f_6=open('/media/ghazal/New Volume/asc_aorta.txt',"w")
f_2=open('/media/ghazal/New Volume/lvs.txt',"w")
f_1=open('/media/ghazal/New Volume/lvd.txt',"w")
f_0=open('/media/ghazal/New Volume/ivsd.txt',"w")
f_7=open('/media/ghazal/New Volume/sinuses.txt',"w")
f_4=open('/media/ghazal/New Volume/root.txt',"w")
f_8=open('/media/ghazal/New Volume/LA.txt',"w")
f_5=open('/media/ghazal/New Volume/lal.txt',"w")
f_3=open('/media/ghazal/New Volume/pwd.txt',"w")

for i in range(109):
    arr = f.readline().split(',')
    name=arr[0][:]
    frame=arr[1]

    for j in range(2,len(arr)-1):
        f_cent = open('/media/ghazal/New Volume/extracted_pairs.txt', "r")
        for k in range(1136):

            arr_1 = f_cent.readline().split(',')
            if arr_1[0][:] == name and arr_1[1] == frame:
                for mes_num in range(j-2):
                    arr_1 = f_cent.readline().split(',')
                f_cent.close()
                break
        if arr[j]=='ivsd':
            for ind in range(len(arr_1)):
                f_0.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_0.write(',')
        elif arr[j] == 'lvd':
            for ind in range(len(arr_1)):
                f_1.write(arr_1[ind])
                if ind != len(arr_1) - 1:
                    f_1.write(',')
        elif arr[j] == 'lvs':
            for ind in range(len(arr_1)):
                f_2.write(arr_1[ind])
                if ind != len(arr_1) - 1:
                    f_2.write(',')
        elif arr[j]=='pwd':
            for ind in range(len(arr_1)):
                f_3.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_3.write(',')
        elif arr[j]=='root':
            for ind in range(len(arr_1)):
                f_4.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_4.write(',')
        elif arr[j]=='lal':
            for ind in range(len(arr_1)):
                f_5.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_5.write(',')
        elif arr[j]=='asc_aorta':
            for ind in range(len(arr_1)):
                f_6.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_6.write(',')
        elif arr[j]=='sinuses':
            for ind in range(len(arr_1)):
                f_7.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_7.write(',')
        elif arr[j]=='LA':
            for ind in range(len(arr_1)):
                f_8.write(arr_1[ind])
                if ind!=len(arr_1)-1:
                    f_8.write(',')
f.close()
f_0.close()
f_1.close()
f_2.close()
f_3.close()
f_4.close()
f_5.close()
f_6.close()
f_7.close()
f_8.close()
