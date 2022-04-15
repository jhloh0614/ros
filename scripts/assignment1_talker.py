#!/usr/bin/env python


import rospy
import os
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=False)
    rate = rospy.Rate(1)  # set rate to 1hz = 1 loop/sec
    counter = 0
    while not rospy.is_shutdown():
        username = os.getlogin()
        str = "%s counter: %d" % (username, counter)
        rospy.loginfo(str)
        pub.publish(str)
        counter += 1
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
