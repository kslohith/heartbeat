# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:18:07 2019

@author: Admin
"""

#import scipy
#import numpy as np
#from scipy.fftpack import fft
## Number of samplepoints
#N = 600
## sample spacing
#T = 1.0 / 800.0
#x = np.linspace(0.0, N*T, N)
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
#yf = fft(y)
#xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
#xint = xf.astype(int)
#yint = yf.astype(int)
#import matplotlib.pyplot as plt
#plt.plot(xint, 2.0/N * np.abs(yint[0:N/2]))
#plt.grid()
#plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:56:17 2018

@author: Dell
"""
#import PESHack
import exppppppppppppppp
import cv2
from scipy import signal
from scipy.fftpack import fft
import numpy as np
from scipy.fftpack import fftfreq
""" i got the hue values from the previous program but i dont know how to automatically plot so copied those values here"""
'''
hue =[]
with open("1.txt") as f:
    for line in f:
        for word in line.split(','):
            hue.append(word)
 '''           
#print(hue)
#print(len(hue))
from matplotlib import pyplot as plt
import math
hue.append(0)
red.append(0)
green.append(0)
blue.append(0)
saturation.append(0)
#value.append(0)


y = fft(hue)
y1 = fft(red)
y2 = fft(green)
y3 = fft(blue)
y4 = fft(saturation)
#y5 = fft(value)


dhue = signal.detrend(hue)
dred= signal.detrend(red)
dgreen = signal.detrend(green)
dblue = signal.detrend(blue)
dsaturation = signal.detrend(saturation)
#dvalue = signal.detrend(value)



yd = fft(dhue)
yd1 = fft(dred)
yd2 = fft(dgreen)
yd3 = fft(dblue)
yd4 = fft(dsaturation)
#yd5 = fft(dvalue)



N = 340
# sample spacing
T = 1.0 / 100.0
x = np.linspace(0.0, N*T, N)

y = np.array(hue)
y1 = np.array(red)
y2 = np.array(green)
y3 = np.array(blue)
y4 = np.array(saturation)
#y5 = np.array(value)


yf = fft(y)
yf1 = fft(y1)
yf2 = fft(y2)
yf3 = fft(y3)
yf4 = fft(y4)
#yf5 = fft(y5)


realyf = yf.real
realyf1 = yf1.real
realyf2 = yf2.real
realyf3 = yf3.real
realyf4 = yf4.real
#realyf5 = yf5.real


yg = np.abs(yd[:N//2])
yg1 = np.abs(yd1[:N//2])
yg2 = np.abs(yd2[:N//2])
yg3 = np.abs(yd3[:N//2])
yg4 = np.abs(yd4[:N//2])
#yg5 = np.abs(yd5[:N//2])


#yg = yg[2:]
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
#xf = xf[2:]
xint = list(xf)
#for i in xint:
#    i = math.ceil(i)
xf1 = xf*10
mylist1 = zip(xf1,yg2)
mydict1 = dict(mylist1)
xarray1 = mydict1.keys()
yarray1 = mydict1.values()
a1=[]
for key in xarray1:
    a1.append(key)
b1 = []
for values in yarray1:
    b1.append(values)
maxheart1 = 0
max1=0
for ij in range(len(b1)):
    if(a1[ij] > 65 and a1[ij] < 120 ):
            if( b1[ij] > max1 ):
                max1 = b1[ij]
                maxheart1 = a1[ij]
        
mylist2 = zip(xf1,yg1)
mydict2 = dict(mylist2)
xarray2 = mydict2.keys()
yarray2 = mydict2.values()
a2=[]
for key in xarray2:
    a2.append(key)
b2 = []
for values in yarray2:
    b2.append(values)
maxheart2 = 0
max2=0
for ij in range(len(b2)):
    if(a2[ij] > 65 and a2[ij] < 120 ):
            if( b2[ij] > max1 ):
                max2 = b2[ij]
                maxheart2 = a2[ij]
                
mylist3 = zip(xf1,yg3)
mydict3 = dict(mylist3)
xarray3 = mydict3.keys()
yarray3 = mydict3.values()
a3=[]
for key in xarray3:
    a3.append(key)
b3 = []
for values in yarray3:
    b3.append(values)
maxheart3 = 0
max3=0
for ij in range(len(b3)):
    if(a3[ij] > 65 and a3[ij] < 120 ):
            if( b3[ij] > max3 ):
                max3 = b3[ij]
                maxheart3 = a3[ij]
                
mylist4 = zip(xf1,yg4)
mydict4 = dict(mylist4)
xarray4 = mydict4.keys()
yarray4 = mydict4.values()
a4=[]
for key in xarray4:
    a4.append(key)
b4 = []
for values in yarray4:
    b4.append(values)
maxheart4 = 0
max4=0
for ij in range(len(b4)):
    if(a4[ij] > 65 and a4[ij] < 120 ):
            if( b4[ij] > max4 ):
                max4 = b4[ij]
                maxheart4 = a4[ij]
                
"""mylist5 = zip(xf1,yg5)
mydict5 = dict(mylist5)
xarray5 = mydict5.keys()
yarray5 = mydict5.values()
a5=[]
for key in xarray5:
    a5.append(key)
b5 = []
for values in yarray5:
    b5.append(values)
maxheart5 = 0
max5=0
for ij in range(len(b5)):
    if(a5[ij] > 65 and a5[ij] < 120 ):
            if( b5[ij] > max1 ):
                max5 = b5[ij]
                maxheart5 = a5[ij]
"""                
mylist0 = zip(xf1,yg)
mydict0 = dict(mylist0)
xarray0 = mydict0.keys()
yarray0 = mydict0.values()
a0=[]
for key in xarray0:
    a0.append(key)
b0 = []
for values in yarray0:
    b0.append(values)
maxheart0 = 0
max0=0
for ij in range(len(b0)):
    if(a0[ij] > 65 and a0[ij] < 120 ):
            if( b0[ij] > max0 ):
                max0 = b0[ij]
                maxheart0 = a0[ij]
                                        


#max_y = max(yg1)  # Find the maximum y value
#max_x = xf1[yg1.index(max_y)]  # Find the x value corresponding to the maximum y value
#print (max_x, max_y)



fig, ax = plt.subplots()
#ax.plot(xf*10-15, yg)
#ax.plot(xf, 2.0/N * np.abs(yd[:N//2]))
#plt.show()

#ax.plot(xf*10-15, yg1)
#ax.plot(xf*10-15, yg2)
ax.plot(xf*10, yg3)
#ax.plot(xf*10, yg4)
#ax.plot(xf*10-5, yg5)

plt.show()

from firebase import firebase

firebase=firebase.FirebaseApplication('https://halo2-1ce47.firebaseio.com/')

result = firebase.put('/Patients/Lohith','heartRate',math.ceil(maxheart3))

print("Heart rate is:" + str(result))
#print(result)


#
#import plotly
#plotly.offline.init_notebook_mode(connected=True)
#import plotly.offline as py
#import plotly.graph_objs as go
#from plotly.tools import FigureFactory as FF
#
#import numpy as np
#import pandas as pd
#import scipy
#import peakutils
#
#
#
#cb = np.array(xf1)
#indices = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=0.1)
#
#trace = go.Scatter(
#    x=[j for j in range(len(xf1))],
#    y=yg1,
#    mode='lines',
#    name='Original Plot'
#)
#
#trace2 = go.Scatter(
#    x=indices,
#    y=[xf1[j] for j in indices],
#    mode='markers',
#    marker=dict(
#        size=8,
#        color='rgb(255,0,0)',
#        symbol='cross'
#    ),
#    name='Detected Peaks'
#)
#
#data = [xf1, yg1]
#py.iplot(data, filename='Vybhav')
#

#plt.figure(figsize=(5, 4))
#plt.plot( hue, label="x")
#plt.plot( dhue, label="x_detrended")
#plt.legend(loc='best')
#plt.show()

#plt.plot(xf, 2.0/N * np.abs(realyf[0:N/2]))
#plt.grid()
#plt.show()



#plt.figure(figsize=(5, 4))
#plt.plot( hue, label="x")
#plt.plot( dhue, label="x_detrended")
#plt.legend(loc='best')
#plt.show()

#plt.plot(xf, 2.0/N * np.abs(realyf[0:N/2]))
#plt.grid()
#plt.show()


