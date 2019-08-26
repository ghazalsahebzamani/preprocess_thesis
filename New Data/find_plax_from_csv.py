import csv
fid=open('/media/ghazal/New Volume/plax_views2.txt','w')
plax_cnt=0
with open('/media/ghazal/01D176301231DAE0/nas/Cardiac data_cleaned/view_quality_label.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    line_count = 0
    for row in reader:
        # print(row[1])
        name = row[0]
        view = row[1]
        if view == '4':
            print(name)
            fid.write(name)
            # fid.write(',')
            fid.write('\n')
            plax_cnt += 1
        line_count += 1
    print(plax_cnt)
    fid.close()
csvFile.close()





#
# with open('/home/ghazal/Downloads/list_view_quality.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#
#     for row in csv_reader:
#         # if line_count == 0:
#         #     # print(f'Column names are {", ".join(row)}')
#         #     line_count += 1
#         # else:
#
#     # print(f'Processed {line_count} lines.')