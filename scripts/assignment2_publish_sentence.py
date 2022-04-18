#!/usr/bin/env python


import sys
import rospy
from std_msgs.msg import String


def publish_sentence(msg):
    # question: why need to initialise topic first, 
    # initialise node first doesn't work.
    pub = rospy.Publisher('sound', String, queue_size=10)
    rospy.init_node('sender', anonymous=False)
    
    rospy.loginfo(rospy.get_caller_id() + ': I sent %s' % msg)
    pub.publish(msg)


if __name__ == '__main__':
    try:
        publish_sentence(sys.argv[1])
    except rospy.ROSInterruptException:
        pass
    except Exception:
        pass