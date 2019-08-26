import glob

# test_impaths = glob.glob('/media/ghazal/01D176301231DAE0/Unet2/LVComb/LA/prepared train_skel/*.jpg')
#
# test_segpaths = glob.glob('/media/ghazal/01D176301231DAE0/Unet2/LVComb/LA/lv_masked/*.png')
#
# fid=open("test_names_la.txt", "w")
# for i in range(78,len(test_impaths)):
#     print(test_impaths[i])
#     fid.write(test_impaths[i])
#     fid.write('\n')
# fid.close()


test_impaths1 = glob.glob('~/Desktop/prepared_train_skel/*.jpg')
test_impaths2 = glob.glob('~/Desktop/prepared_train/*.jpg')
# test_segpaths = glob.glob('/media/ghazal/01D176301231DAE0/Unet2/LVComb/LA/lv_masked/*.png')
print(len(test_impaths1))
print(len(test_impaths2))
# fid=open("test_dataset_names_lv.txt", "w")
for i in range(175,len(test_impaths1)):
    print(test_impaths1[i])

    print(test_impaths2[i])

