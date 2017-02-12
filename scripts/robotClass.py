#!/usr/bin/env python
"""
@author: S. Bertrand

# all variables in SI unit
"""

# **** TO DO: put encoderResolution, wheel diameter and inter wheels dist as parameters (YAML)


class Odometer:
    
    def __init__(self):
        self.leftWheelTheta = 0.0
        self.rightWheelTheta = 0.0
        self.leftWheelThetaPrec = 0.0
        self.rightWheelThetaPrec = 0.0


class Wheel:
    
    def __init__(self, diameter):
        self.diameter = diameter
        self.v = 0.0
        self.omega = 0.0
        self.omegaRef = 0.0
        self.encoderCount = 0
        self.encoderCountPrev = 0
        self.lastTimeCountChange = 0.0
        self.encoderResolution = 20 #nb of counts per revolution
        

class Robot:
    
    def __init__(self, interWheelDistance, wheelDiameter, x0=0.0, y0=0.0, theta0=0.0):
    # zero inital speed and angular velocity assumed
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.theta0 = theta0
        self.theta = theta0
        self.v = 0.0
        self.vRef = 0.0
        self.omega = 0.0
        self.omegaRef = 0.0
        self.interWheelDistance = interWheelDistance
        self.leftWheel = Wheel(wheelDiameter)
        self.rightWheel = Wheel(wheelDiameter)
        self.odometer = Odometer()


if __name__=='__main__':
    ardupiRobot = Robot(0.15, 0.05)