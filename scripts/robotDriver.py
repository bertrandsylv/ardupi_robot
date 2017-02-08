#!/usr/bin/env python
"""
@author: S. Bertrand

# main script: robot driver

# all variables in SI unit

"""

import rospy
from geometry_msgs.msg import Twist, TwistStamped
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
pubLeftWheelSpeed = rospy.Publisher('ardupi_robot/wheelSpeed/left', TwistStamped, queue_size=10)
pubRightWheelSpeed = rospy.Publisher('ardupi_robot/wheelSpeed/right', TwistStamped, queue_size=10)
# odometry estimated from wheel encoders 
pubOdometry = rospy.Publisher('ardupi_robot/odom', Odometry, queue_size=10)
# publish on these topics to send control values to the robot  (in [-255,+255])
pubLeftMotorCmd = rospy.Publisher('ardupi_robot/cmdMotor/left', Int32Stamped, queue_size=10)
pubRightMotorCmd = rospy.Publisher('ardupi_robot/cmdMotor/right', Int32Stamped, queue_size=10)


# subscribers callbacks
# ----------------------

def callBackLeftEncoderCount(data):
    global robot
    msgTwist = TwistStamped()    
    
    msgTwist.header = data.header
    
    robot.leftWheel.encoderCount = data.data 
    t = data.header.stamp.secs + 1.E-9*data.header.stamp.nsecs
    deltaT = t-robot.leftWheel.lastTimeCountChange
    print deltaT
#    print robot.leftWheel.encoderCount
#    rospy.loginfo(rospy.get_name() + " - time: %f" % t)
    
    # angular speed computation
    if (deltaT>0.0):
        robot.leftWheel.omega = (robot.leftWheel.encoderCount - robot.leftWheel.encoderCountPrev)*(2.0*np.pi/robot.leftWheel.encoderResolution) / deltaT
        robot.leftWheel.lastTimeCountChange = t
        robot.leftWheel.encoderCountPrev = robot.leftWheel.encoderCount
        print robot.leftWheel.omega
        
        msgTwist.twist.angular.z = robot.leftWheel.omega
        pubLeftWheelSpeed.publish(msgTwist)
        
        

def callBackRightEncoderCount(data):
    global robot    
    robot.rightWheel.encoderCount = data.data

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

