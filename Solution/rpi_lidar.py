#!/usr/bin/env python3
import math
import rospy
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt

arena_length = 0.97     # in metres
arena_width = 0.58      # in metres
lidar_diameter = 0.08   # in metres



def pos_calc(n,s,height):
    if math.isinf(n) and math.isinf(s):
        return math.inf
    
    if math.isinf(n) and not math.isinf(s):
        return s
    
    if math.isinf(s) and not math.isinf(n):
        return height - n
    
    else:
        return (s + height - n)/2 
    

def laser_cb(data):
    min_angle = data.angle_min
    max_angle = data.angle_max
    ang_increment = data.angle_increment
    UL = (max_angle-min_angle)/ang_increment

    n = data.ranges[int(0)]
    s = data.ranges[int(UL/2)]
    w = data.ranges[int(UL/4)]
    e = data.ranges[int(3*UL/4)]

    print("x position :{}".format(pos_calc(e,w,arena_width)))
    print("Y position :{}".format(pos_calc(n,s,arena_length)))
    plt.scatter(pos_calc(e,w,arena_width),pos_calc(n,s,arena_length))
    plt.pause(0.05)


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