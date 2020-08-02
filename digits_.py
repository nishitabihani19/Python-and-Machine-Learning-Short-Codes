from sklearn.datasets import load_digits
from sklearn import svm
import matplotlib.pyplot as plt
digit=load_digits()
#print(digit.data)
clf=svm.SVC(gamma=0.001,
        C=100)
x=digit.data
y=digit.target
clf.fit(x,y)
n1=(clf.predict(digit.data))
#print(n1[3])
#print(n1[-5])
#print(x[-5])
#plt.imshow(digit.images[-5])
plt.imshow(digit.images[-5],cmap=plt.cm.gray_r)
plt.show()
