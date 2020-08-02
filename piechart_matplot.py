import matplotlib.pyplot as plt
subject=['math','phy','chem','bio']
marks=[80,50,30,100]
color=['green','blue','yellow','red']
xplot=(0,0,0,0.2)
fig,ax1=plt.subplots()
ax1.pie(marks,
        explode=xplot,
        autopct='%1.1f%%',
        pctdistance=0.5,
        shadow=True,
        labeldistance=1.1,
        colors=color,
        radius=1,
        counterclock=True,
        rotatelabels=False,
        startangle=90,
        labels=subject)
ax1.axis('equal')
plt.show()

