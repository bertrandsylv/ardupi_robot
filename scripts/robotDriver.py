#!/usr/bin/env python
"""
@author: S. Bertrand

# main script: robot driver

# all variables in SI unit

"""

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from ardupi_robot.msg import Int32Stamped # for receiving navdata feedback
import numpy as np
import robotClass


# node init
# ----------
rospy.init_node('ardupi_robot_driver', anonymous=True)


# robot object
# ------------
robot = robotClass.Robot(interWheelDistance=0.15, wheelDiameter=0.05, x0=0.0, y0=0.0, theta0=0.0)



# publishers
# -----------
# wheel speed estimated from wheel encoders (linear and angular)
pubLeftWheelSpeed = rospy.Publisher('ardupi_robot/wheelSpeed/left', Twist, queue_size=10)
pubRightWheelSpeed = rospy.Publisher('ardupi_robot/wheelSpeed/right', Twist, queue_size=10)
# odometry estimated from wheel encoders 
pubOdometry = rospy.Publisher('ardupi_robot/odom', Odometry, queue_size=10)
# publish on these topics to send control values to the robot  (in [-255,+255])
pubLeftMotorCmd = rospy.Publisher('ardupi_robot/cmdMotor/left', Int32Stamped, queue_size=10)
pubRightMotorCmd = rospy.Publisher('ardupi_robot/cmdMotor/right', Int32Stamped, queue_size=10)


# subscribers callbacks
# ----------------------

def callBackLeftEncoderCount(data):
    global robot
    print data

def callBackRightEncoderCount(data):
    global robot    
    print data

def callBackCmdVel(data):
    global robot    
    print data
   
   
# subscribers
# ------------
rospy.Subscriber("ardupi_robot/countEncoder/left", Int32Stamped, callBackLeftEncoderCount)
rospy.Subscriber("ardupi_robot/countEncoder/right", Int32Stamped, callBackRightEncoderCount)
rospy.Subscriber("ardupi_robot/cmd_vel", Twist, callBackCmdVel)



# main node loop
# ---------------
if __name__ == '__main__':
    rospy.spin()
    # TO DO: loop at a given frequency
