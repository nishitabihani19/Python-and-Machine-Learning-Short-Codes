#web Scrapping
from sklearn.datasets import load_iris
iris=load_iris()
import numpy as np
from sklearn import tree

training=iris.data
label=iris.target
#testing=[[5.1,3.5,1.4,0.2]]
#testing=[[5.9,3.,5.1,1.8]]
c
clf=tree.DecisionTreeClassifier()
decision=clf.fit(training,label)
result=decision.predict(testing)
print(iris.target)
print(iris.target==result)
#print(iris.target_names[result[0]])

