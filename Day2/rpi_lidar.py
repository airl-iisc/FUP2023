#!/usr/bin/env python3
import math
import rospy
from sensor_msgs.msg import LaserScan

arena_length = 0.97     # in metres
arena_width = 0.58      # in metres
lidar_diameter = 0.08   # in metres
  

def laser_cb(data):
    theta_min = data.angle_min
    theta_max = data.angle_max
    theta_resolution = data.angle_increment

    ############################################
    #### Insert your code within these tags ####
    ############################################
    #
    # Your code here:
    # 
    # 
    # dist_k = data.ranges[int(k)]
    #
    #
    #
    ##############################################
    #### Output X Coordinate and Y Coordinate ####
    ##############################################


    # Calculate x position
    print("X {}".format(x_coordinate))
    # Calculate y position
    print("Y {}".format(y_coordinate))


# You do not need to modify code below this line

def scanner_node():
    rospy.init_node('laser_scanner',anonymous=True)
    rospy.loginfo("laser Node  Starting...")
    laser_sub = rospy.Subscriber("/scan",LaserScan,laser_cb)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        scanner_node()
    except rospy.ROSInterruptException:
        pass