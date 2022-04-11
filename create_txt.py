#coding=utf-8

txtName = '/home/zhangcz/local_code/work/HOG_SVM/dataset/train/image/train.txt'
f=file(txtName, "a+")
for i in range(1,1001):
    if i <= 500:
        new_context = 'cat' + str(i-1) + '.jpg' + ' ' + '0' + '\n'
        f.write(new_context)
    else:
        new_context = "dog" + str(i-501) + '.jpg' + ' ' + '1' + '\n'
        f.write(new_context)
f.close()