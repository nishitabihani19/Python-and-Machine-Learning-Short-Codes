import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
x=['python','c','java','pearl','ml','datascience']
y=[10,8,9,4,2,5]
z=[4,6,8,3,4,2]
v=[1,2,3,2,2,3]
plt.bar(x,y)
plt.bar(x,z)
#plt.barh(x,v)
plt.bar(x,v)
plt.xlabel('language')
plt.ylabel('performance')
plt.title('lang_per')

plt.show()
