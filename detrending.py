
import cv2
from scipy import signal

""" i got the hue values from the previous program but i dont know how to automatically plot so copied those values here"""

hue = [
76.22384765625,
76.75094075520833,
77.92081705729167,
76.00044596354167,
79.75417317708333,
82.45720703125,
84.027939453125,
87.85794270833334,
88.80732747395834,
91.02869791666667,
92.23721354166666,
93.27419921875,
89.91781901041666,
86.98552734375,
89.12044921875,
86.77469401041667,
81.16447916666667,
86.25272135416667,
80.98942708333334 ]

dhue = signal.detrend(hue)    
from matplotlib import pyplot as plt
plt.figure(figsize=(5, 4))
plt.plot( hue, label="x")
plt.plot( dhue, label="x_detrended")
plt.legend(loc='best')
plt.show()
