# HOG+SVM

上面的hog_svm.py是用于训练的，通过提取图片的hog特征，然后通过SVM进行训练得到model，最后通过model进行预测,将结果写入result.txt文件之中。

不要将hog的参数设置的太复杂。不然提取的特征会非常大，然后训练的时候会占满内存，导致机器死机。