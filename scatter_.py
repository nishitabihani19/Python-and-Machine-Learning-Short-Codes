import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.rcParams["figure.figsize"]=(16,9)
a=make_blobs()
x,y=make_blobs(n_samples=50,n_features=3)
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x[:,0],x[:,1],x[:,2])
kmeans=KMeans(n_clusters=4)
kmeans=kmeans.fit(x)
labels=kmeans.predict(x)
c=kmeans.cluster_centers_
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x[:,0],x[:,1],x[:,2],c=y)
ax.scatter(c[:,0],c[:,1],c[:,2],marker="*",s=1000)
plt.show()
