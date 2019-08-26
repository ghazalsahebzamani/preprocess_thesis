import numpy as np



fid=open('/media/ghazal/New Volume/plax_views2.txt','r')

fid2=open('/media/ghazal/New Volume/unique_plax_views2.txt','w')
names_arr=[]
for i in range(371065):
    print(i)
    path=fid.readline()
    names_arr.append(path[:-1])
print("hi",len(names_arr))
unique_path=list(set(names_arr))
print(len(unique_path))

from collections import Counter

a = dict(Counter(names_arr))
num_list=list(a.values())
print(np.sum(num_list))
# >>> print a           #or print(a) in python-3.x
# {'a': 3, 'c': 3, 'b': 1}
for i in range(len(unique_path)):
    fid2.write(unique_path[i])
    fid2.write('\n')
fid2.close()
fid.close()