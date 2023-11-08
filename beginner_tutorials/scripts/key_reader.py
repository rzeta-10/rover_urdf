#!/usr/bin/env python3

import sys
import tty
import termios
import time
import rospy
#ros msgs
from geometry_msgs.msg import Twist
# from std_msgs.msg import String


def getTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)


def readKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

rospy.init_node('rc_control',anonymous=True)

cmd_vel= rospy.Publisher('/cmd_vel',Twist,queue_size=20)
# rc_dir_pub= rospy.Publisher('/dir_selection',Int32,queue_size=20)

if __name__ == '__main__':

    settings=getTerminalSettings()

    try:
        
        r = rospy.Rate(10)
        key='\0'
        twist_msg = Twist()

        twist_msg.linear.x = 0.0
        cmd_vel.publish(twist_msg)
        print("Velocity published: linear.x = ", twist_msg.linear.x)


        while True:
        
            key=readKey(settings)
            
            if key == 'w':
                twist_msg.linear.x = twist_msg.linear.x+0.01
                print("Velocity published: linear.x = ",twist_msg.linear.x)
            elif key == 's':
                twist_msg.linear.x = twist_msg.linear.x+-0.01
                print("Velocity published: linear.x = ",twist_msg.linear.x)
            else:
                
                print("velocity published is null")
            
            if key == 'd':
                twist_msg.angular.z = twist_msg.angular.z+0.01
                print("Changing direction : ",twist_msg.angular.z)
            elif key == 'a':
                twist_msg.angular.z = twist_msg.angular.z+-0.01
                print("Changing direction : ",twist_msg.angular.z)
            else:
                
                print("No change in direction published")
            cmd_vel.publish(twist_msg)
            if key=='p':
                break
            
            r.sleep()
            
        print("controller terminated")
                
            
            
    except KeyboardInterrupt:
        print("interupted!!!")

    except Exception as e:
        print(e)