import glob
test_impaths1 = glob.glob('~/Desktop/prepared_train_skel/*.jpg')
test_impaths2 = glob.glob('~/Desktop/prepared_train/*.jpg')
print(len(test_impaths1))
print(len(test_impaths2))
for i in range(175,len(test_impaths1)):
    print(test_impaths1[i])

    print(test_impaths2[i])

