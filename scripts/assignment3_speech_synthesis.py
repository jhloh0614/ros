#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from gtts import gTTS
import os

def callback(data):
    rospy.loginfo('Speech synthesis start')
    msg = data.data
    rospy.loginfo(rospy.get_caller_id() + ': I received %s' % (msg))

    reply = generate_reply(msg)

    tts = gTTS(reply)

    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
    os.remove("speech.mp3")
    rospy.loginfo('Speech synthesis end')
    rate = rospy.Rate(3)
    rate.sleep()

def sound_play():
    rospy.init_node('robot001', anonymous=False)
    rospy.Subscriber('result', String, callback=callback)
    rospy.spin()


def generate_reply(msg):
    msg = str.lower(msg)
    rospy.loginfo(msg)
    ans = 'a'
    if msg == 'who are you':
        ans = 'I am Robot 001. May I know your name?'
    elif msg == 'i am jack':
        ans = 'Nice to meet you Jack!'
    else:
        ans ="I can't hear you."
    return ans
    


if __name__ == '__main__':
    sound_play()