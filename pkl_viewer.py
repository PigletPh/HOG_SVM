import pickle
#doc = open('/home/zhangcz/local_code/work/HOG_SVM/model/a.txt', 'a')  #打开一个存储文件，并依次写入
test = open('/home/zhangcz/local_code/work/HOG_SVM/model/clf.pkl','rb')
data = pickle.load(test)
#print(data, file = doc)
