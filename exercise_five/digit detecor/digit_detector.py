#!/usr/bin/env python3

import os
import numpy as np
import cv2
import yaml
import tf
import math
import numpy as np
from cv_bridge import CvBridge
from collections import deque
from turbojpeg import TurboJPEG, TJPF_GRAY
from dt_apriltags import Detector
from duckietown_msgs.msg import AprilTagDetectionArray, AprilTagDetection
from duckietown_msgs.srv import GetVariable

import rospy

from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage, CameraInfo
from geometry_msgs.msg import Transform, Vector3, Quaternion
from std_msgs.msg import String, Int32

import model


class DigitDetectorNode(DTROS):
    def __init__(self, node_name):
        super(DigitDetectorNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        name = os.environ['VEHICLE_NAME']
        # self.image_sub = rospy.Subscriber(f'/{name}/camera_node/image/compressed', CompressedImage, self.callback,  queue_size = 1)
        self.image_sub = rospy.Subscriber(f'/{name}/digit_detector_node/image/compressed', CompressedImage, self.callback,  queue_size = 1)
        self.img_queue = deque(maxlen=1)
        self.bridge = CvBridge()
        self.digit_pub = rospy.Publisher(f'/{name}/digit', Int32,  queue_size = 1)

    def callback(self, msg):
        image = self.bridge.compressed_imgmsg_to_cv2(msg)
        self.img_queue.append(image)
        rospy.loginfo('Image received...')

    def run(self): 
        rate = rospy.Rate(4) # 5Hz
        while not rospy.is_shutdown():
            if self.img_queue:
                img = self.img_queue.popleft()  
                self.detect_digit(img)
            rate.sleep()

    
    def detect_digit(self, img):
        digit = model.run(img)
        self.digit_pub.publish(digit)
        # rospy.loginfo(f'Digit: {digit}')
        

    
if __name__ == '__main__': 
    digit_detector = DigitDetectorNode(node_name='digit_detector_node')
    digit_detector.run()
    rospy.spin()
