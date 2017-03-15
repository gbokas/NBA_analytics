import pandas as pd
import numpy as np
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
from lxml import objectify
import sqlite3
style.use('ggplot')

df=pd.read_csv('nbatotal.csv')
height=((df["Ht"].str.split('-')))
inches_tot=np.array(height)
inches=np.array([int(l[0]) for l in inches_tot])
inches_sm=np.array([int(l[1]) for l in inches_tot])
meters=inches*30.48+inches_sm*2.54
k=0
results=[]
gia_plot=[]
minimum=max(df["FT%"])
print(minimum)
for i in range (160,250,5):
    average=0
    p=0
    for j in range (1, 507, 1):
        if meters[j]>i and meters[j]<i+5:
            average=average+df["FT%"][j]
            p=p+1
    if p!=0:
        k=k+1
        results.append(i)
        gia_plot.append(average/p)
        print(i,average/p)
axis_font = {'fontname':'Arial', 'size':'18'}
plt.plot(results,gia_plot,linewidth=3.0, color='b',alpha=0.75)
plt.scatter(meters,df["FT%"],df["FTA"]/25, c=df["COLOR"])
plt.text(198.12, 0.835, 'MJ',**axis_font)
plt.text(203.2, 0.742, 'LJ',**axis_font)
plt.text(205.74, 0.414, 'Ben Wallace',**axis_font)
plt.text(205.74, 0.851, 'Magic',**axis_font)
plt.text(190.5, 0.904, 'Steve Nash',**axis_font)
plt.grid(True)
plt.xlabel("Height (m)", fontsize=22, color='black')
plt.ylabel("FT%", fontsize=22,color='black')
plt.xscale("log")
plt.savefig("trial.eps")
plt.show()
