#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from gtts import gTTS
import os

def callback(data):
    msg = data.data
    rospy.loginfo(rospy.get_caller_id() + ': I received %s' % (msg))

    tts = gTTS(msg)

    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
    os.remove("speech.mp3")

def sound_play():
    rospy.init_node('player', anonymous=False)
    rospy.Subscriber('sound', String, callback=callback)
    rospy.spin()


if __name__ == '__main__':
    sound_play()
