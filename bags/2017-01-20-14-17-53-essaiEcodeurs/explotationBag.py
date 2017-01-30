# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:06:01 2017

@author: Hoagie
"""

import numpy as np
import matplotlib.pyplot as plt

RES = 20.0

dataLeftEncoder = np.loadtxt("_slash_ardupi_robot_slash_countEncoder_slash_left.csv", delimiter=",", skiprows=1, usecols=(0,2,4,5,7))
dataRightEncoder = np.loadtxt("_slash_ardupi_robot_slash_countEncoder_slash_right.csv", delimiter=",", skiprows=1, usecols=(0,2,4,5,7))


countLeftEncoder = dataLeftEncoder[:,4]
timeLeftEncoder = dataLeftEncoder[:,2]-dataLeftEncoder[0,2] + (dataLeftEncoder[:,3]*1E-9)
countRightEncoder = dataRightEncoder[:,4]
timeRightEncoder = dataRightEncoder[:,2]-dataRightEncoder[0,2] + (dataRightEncoder[:,3]*1E-9)

plt.figure()
plt.plot(timeLeftEncoder, countLeftEncoder, label='left')
plt.plot(timeRightEncoder, countRightEncoder, label='right')
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('Encoder count')
plt.legend()



speedLeftEncoder = np.zeros_like(countLeftEncoder)
filteredSpeedLeftEncoder = np.zeros_like(countLeftEncoder)
for i in range(1,len(speedLeftEncoder)):
    if (timeLeftEncoder[i]!=timeLeftEncoder[i-1]):
        #print timeLeftEncoder[i]-timeLeftEncoder[i-1]
        speedLeftEncoder[i] = (countLeftEncoder[i]-countLeftEncoder[i-1])*(2.0*np.pi/RES)/(timeLeftEncoder[i]-timeLeftEncoder[i-1])
        if (i>=5):
            filteredSpeedLeftEncoder[i] = np.median(speedLeftEncoder[i-4:i])
        else:
            filteredSpeedLeftEncoder[i] = np.median(speedLeftEncoder[0:i])
            

speedRightEncoder = np.zeros_like(countRightEncoder)
for i in range(1,len(speedRightEncoder)):
    if (timeRightEncoder[i]!=timeRightEncoder[i-1]):
        speedRightEncoder[i] = (countRightEncoder[i]-countRightEncoder[i-1])*(2.0*np.pi/RES)/(timeRightEncoder[i]-timeRightEncoder[i-1])

plt.figure()
plt.plot(timeLeftEncoder, speedLeftEncoder, label='left')
plt.plot(timeLeftEncoder, filteredSpeedLeftEncoder, label='med. filt. left')
plt.plot(timeRightEncoder, speedRightEncoder, label='right')
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('Angular speed (rad/s)')
plt.legend()

plt.show()
