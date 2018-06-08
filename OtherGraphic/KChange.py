from tkinter import messagebox

from GUI import *
from GUI import Initialize

from KMap.TopKSearch import topKSearch
import matplotlib.pyplot as plt



def kChange():
    x = Initialize.initialize()
    lats = (int)(x.enter_latidtude.get())
    lons = (int)(x.enter_longitude.get())
    times=[]
    k=[1,2,3,5,10,50,100,300,500,1000,3000,5000,10000,15000,20000,25000]
    if (lats > 180 or lats < -180 or lons < -180 or lons > 180):
        messagebox.askyesno("error", "经纬度不合法")
        return
    for x in k:
        lon_result, lat_result, final_result, time = topKSearch(lats, lons, x)
        times.append(time)
    plt.plot(k, times, label='k_change', linewidth=1, color='r', marker='o',
             markerfacecolor='black', markersize=4)
    plt.xlabel('k')
    plt.ylabel('time (s)')
    plt.legend()
    plt.show()