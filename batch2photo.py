# coding=utf-8
import numpy as np
import imageio  # 引入imageio包


# 解压 返回解压后的字典
def unpickle(file):
    import pickle as pk
    fo = open(file, 'rb')
    dict = pk.load(fo)
    fo.close()
    return dict


# 生成训练集图片
for j in range(1, 2):
    dataName = "/home/zhangcz/local_code/work/HOG_SVM/cifar-10-python/cifar-10-batches-py/data_batch_" + str(j)  # 读取当前目录下的data_batch1~5文件。
    Xtr = unpickle(dataName)
    print(dataName + " is loading...")

    for i in range(0, 10000):
        img = np.reshape(Xtr['data'][i], (3, 32, 32))  # Xtr['data']为图片二进制数据
        img = img.transpose(1, 2, 0)  # 读取image
        picName = '/home/zhangcz/local_code/work/HOG_SVM/cifar-10-python/cifar-10-batches-py/train/' + str(Xtr['labels'][i])  + str(i + (j - 1) * 10000) + '.jpg'
        imageio.imsave(picName, img)  # 使用的imageio的imsave类
    print(dataName + " loaded.")

print("test_batch is loading...")

# 生成测试集图片
testXtr = unpickle("/home/zhangcz/local_code/work/HOG_SVM/cifar-10-python/cifar-10-batches-py/test_batch")
for i in range(0, 10000):
    img = np.reshape(testXtr['data'][i], (3, 32, 32))
    img = img.transpose(1, 2, 0)
    picName = '/home/zhangcz/local_code/work/HOG_SVM/cifar-10-python/cifar-10-batches-py/test/' + str(testXtr['labels'][i]) +  str(i) + '.jpg'
    imageio.imsave(picName, img)
print("test_batch loaded.")