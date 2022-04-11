# -*- coding: utf-8 -*-
# 修改文件夹中图像的名字，重新命名
import os

path = '/home/zhangcz/local_code/work/HOG_SVM/dataset/train/image/cats/'
filelist = os.listdir(path)
count = 0
for file in filelist:
    print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    Newdir = os.path.join(path, 'cat'+str(count).zfill(2) + filetype)
    os.rename(Olddir, Newdir)

    count += 1