#!/usr/bin/env python3

import os
import numpy as np
import cv2
from cv_bridge import CvBridge
from collections import deque

import rospy

from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage


class ImageSubscriberPublisherNode(DTROS):
    def __init__(self, node_name):
        super(ImageSubscriberPublisherNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # Subscribe to duckie-bot camera
        self.sub = rospy.Subscriber(f'/{os.environ['VEHICLE_NAME']}/camera_node/image/compressed', CompressedImage, self.callback,  queue_size = 1)
        # Publish image from our node
        self.pub = rospy.Publisher(f'/{os.environ['VEHICLE_NAME']}/my_published_image/compressed', CompressedImage, queue_size = 1)
        self.bridge = CvBridge()
        # Create a queue to receive image. Later, publish the last image based on the given frequency
        self.img_queue = deque(maxlen=1)

    def callback(self, ros_data):
        image = self.bridge.compressed_imgmsg_to_cv2(ros_data)
        # Add the image to img_queue
        self.img_queue.append(image)
        rospy.loginfo(f'Image size: {image.shape}')


    def run(self):
        # publish 15 images every second
        rate = rospy.Rate(15)
        while not rospy.is_shutdown():
            if self.img_queue:
                message = self.img_queue.popleft() 
                img = self.bridge.cv2_to_compressed_imgmsg(message)
                self.pub.publish(img)
            rate.sleep()

if __name__ == '__main__':
    # create the node
    node = ImageSubscriberPublisherNode(node_name='my_subscriber_publisher_node')
    node.run()
    # keep spinning
    rospy.spin()


