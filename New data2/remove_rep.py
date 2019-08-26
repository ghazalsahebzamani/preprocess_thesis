
fid=open('/media/ghazal/New Volume/unique_raw_plax_paths3.txt','r')
prev_found=[]


fid2=open('/media/ghazal/New Volume/unique_raw_plax_paths4.txt','r')

fid3=open('/media/ghazal/New Volume/new_unique_raw_plax_paths4.txt','w')
prev_found2=[]
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
cnt=0
for i in range(13020):
    arr=fid.readline()
    # prev_found.append(arr)
    slash_ind=find(arr,'/')
    folder_slash=slash_ind[-2]
    name=arr[folder_slash:-1]
    prev_found.append(name)
for i in range(19458):
    arr=fid2.readline()
    # slash_ind=find(arr,'/')
    # folder_slash=slash_ind[-2]
    # name=arr[folder_slash:-1]
    # prev_found2.append(name)
    prev_found2.append(arr)
for i in range(len(prev_found2)):
    slash_ind=find(prev_found2[i],'/')
    folder_slash=slash_ind[-2]
    name=prev_found2[i][folder_slash:-1]
    if name not in prev_found:
        fid3.write(prev_found2[i])
    else:
        cnt=cnt+1
    print(cnt)
fid.close()
fid2.close()
fid3.close()
