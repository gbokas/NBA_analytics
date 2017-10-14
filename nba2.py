import pandas as pd
import numpy as np
import datetime
import math
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

perc = np.array(df['FT%'])
perc2 = np.array(df['2P%'])
perc3 = np.array(df['3PA'])
perc4 = np.array(df['3P%'])


perc4 = [x for x in perc4 if not math.isnan(x)]
perc5=[]
for i in range(0, len(perc3)):
  if perc3[i] != 0:
      perc5.append(perc2[i])
    
print(np.mean(perc), np.mean(perc2))
plt.scatter(perc5, perc4)
plt.show()
#percentages = np.array(df["FT%"])
#percentages2 = np.array(df["2P%"])
#print(height)

#plt.plot(percentages)
#plt.show()


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
