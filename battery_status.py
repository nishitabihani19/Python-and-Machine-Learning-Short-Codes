
import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

if plugged==False:
     plugged="Not Plugged In"
else:
     plugged="Plugged In"

print(percent+'% | '+plugged)
'''
import psutil
#print(psutil.cpu_percent())

b=psutil.virtual_memory()
print(b)
'''

