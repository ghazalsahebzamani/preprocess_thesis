import csv
fid=open('/media/ghazal/New Volume/plax_views2.txt','w')
plax_cnt=0
with open('/home/ghazal/Downloads/list_view_quality.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # if line_count == 0:
        #     # print(f'Column names are {", ".join(row)}')
        #     line_count += 1
        # else:
        name=row[0]
        view=row[2]
        if view=='4':
            print(name)
            fid.write(name)
            # fid.write(',')
            fid.write('\n')
            plax_cnt+=1
        line_count += 1
    print(plax_cnt)
    fid.close()
    # print(f'Processed {line_count} lines.')