# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:06:01 2017

@author: Hoagie
"""

import numpy as np
import matplotlib.pyplot as plt

RES = 20.0

dataOmegaRefRight = np.loadtxt("_slash_ardupi_robot_slash_omegaRef_slash_right.csv", delimiter=",", skiprows=1, usecols=(0,1))

dataOmegaRight = np.loadtxt("_slash_ardupi_robot_slash_wheelSpeed_slash_right.csv", delimiter = ",", skiprows=1, usecols=(4,5,15))

omegaRefRight = dataOmegaRefRight[:,1]
timeOmegaRefRight = (dataOmegaRefRight[:,0]-dataOmegaRefRight[0,0])*1.E-9

timeOmegaRight = dataOmegaRight[:,0]-dataOmegaRight[0,0] + (dataOmegaRight[:,1]*1E-9)
omegaRight = dataOmegaRight[:,2]


plt.figure()
plt.plot(timeOmegaRight, omegaRight, label='true')
plt.plot(timeOmegaRefRight, omegaRefRight, label='ref')
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('Omega (rad/s)')
plt.legend()


plt.show()
