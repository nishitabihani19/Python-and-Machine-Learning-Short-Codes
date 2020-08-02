from sklearn import tree
'''
trainingData=[[170,5],[180,5.5],[270,4],[300,3.5]]
label=['domestic','domestic','sports','sports']
testingData=[[160,3]]
clf=tree.DecisionTreeClassifier()
decision=clf.fit(trainingData,label)
result=decision.predict(testingData)
print(result)
#orangeapple
'''
trainingData=[[120,0],[130,0],[170,1],[180,1]]
label=['a','a','o','0']
testingData=[[140,0]]
clf=tree.DecisionTreeClassifier()
decision=clf.fit(trainingData,label)
result=decision.predict(testingData)
print(result)
