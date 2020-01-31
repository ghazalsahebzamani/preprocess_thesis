import numpy as np
f2=open('/media/ghazal/New Volume/dist_to_measures4.txt',"r")
f3=open('/media/ghazal/New Volume/col_indcs2.txt',"r")

for i in range(312):
    dist_arr=f2.readline().split(',')[1:-1]
    new_dist_arr=np.zeros(len(dist_arr))
    for i in range(len(dist_arr)):
        new_dist_arr[i]=float(dist_arr[i])

    print(new_dist_arr)
