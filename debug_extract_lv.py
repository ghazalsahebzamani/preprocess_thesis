f=open('/media/ghazal/New Volume/LV3_combined_cm_dist_after_sort.txt',"r")
test=[]
for i in range(57):
    arr = f.readline().split(',')
    test.append(arr[0])
test=list(dict.fromkeys(test))
print(len(test))