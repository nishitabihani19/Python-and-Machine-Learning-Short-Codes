from sklearn.datasets import load_iris
iris=load_iris()
#print(iris)
#print(dir(iris))
#print(dir(iris.DESCR))
#print(iris.data)
#print(len(iris.data))
#print(iris.feature_names)
#print(iris.target)
#print(iris.target_names)

import numpy as np
from sklearn import tree
unknown=[0,50,100]
training=np.delete(iris.data,unknown,axis=0)#axis=0 is horizontal
label=np.delete(iris.target,unknown)#vertical
#testing=[[5.1,3.5,1.4,0.2]]
#testing=[[5.9,3.,5.1,1.8]]
testing=[iris.data[100]]
clf=tree.DecisionTreeClassifier()
decision=clf.fit(training,label)
result=decision.predict(testing)
print(result)
print(iris.target_names[result[0]])
