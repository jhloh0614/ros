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
    rospy.signal_shutdown('process finished')

def speak(msg):
    tts = gTTS(msg)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
    os.remove("speech.mp3")

def sound_play():
    rospy.init_node('robot001', anonymous=False)
    rospy.Subscriber('result', String, callback=callback)
    greetings = 'Hi, how can I help you?'
    speak(greetings)
    rospy.spin()

    
    
    
def generate_reply(msg):
    name = msg.split(' ')[-1]
    text_file = open('/home/jhloh/catkin_ws/src/beginner_tutorials/name.txt', 'w')
    text_file.write(name)
    text_file.close()
    msg = str.lower(msg)
    rospy.loginfo(msg)
    ans = 'Okay, I will help you find %s' %name
    return ans
    


if __name__ == '__main__':
    sound_play()