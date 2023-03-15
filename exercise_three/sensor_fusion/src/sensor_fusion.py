#!/usr/bin/env python3
import rospy

from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String
from duckietown_msgs.msg import Pose2DStamped, AprilTagDetectionArray
from tf import TransformBroadcaster
import tf2_ros
import tf
from deadreckoning.srv import updatepos
from duckietown_msgs.srv import ChangePattern


class Localization(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(Localization, self).__init__(node_name='localization_node', node_type=NodeType.GENERIC)

        self.veh = rospy.get_param("~veh")

        # Setup services
        self.loginfo("looking for service")

        # Look for teleport service
        rospy.wait_for_service('/' + self.veh + '/update_pos')
        self.update_pos_client = rospy.ServiceProxy('/' + self.veh + '/update_pos', updatepos)

        # Look for LED service
        rospy.wait_for_service('/' + self.veh + '/led_emitter_node/set_pattern')
        self.update_led_client = rospy.ServiceProxy('/' + self.veh + '/led_emitter_node/set_pattern', ChangePattern)

        self.loginfo("Service Found")


        # construct publisher
        self.sub = rospy.Subscriber("/" + self.veh + '/apriltag_detector_node/detections', AprilTagDetectionArray,
                                    self.callback)

        self.tfBuffer = tf2_ros.Buffer(cache_time=rospy.Duration(1))
        self.listener = tf2_ros.TransformListener(self.tfBuffer)
        self.bc = TransformBroadcaster()
        self.loginfo("Initialized")


        self.current_led = 'WHITE'
        self.led_dict = {'GREEN': (93, 94, 200, 201),
                         'RED': (162, 169),
                         'BLUE': (62, 58, 133, 153)}

    def change_led(self, color):
        if self.current_led == color:
            return
        else:
            self.current_led = color
            self.update_led_client(String(color))

    def callback(self, msg):
        if len(msg.detections) == 0:
            self.change_led('WHITE')
            return

        else:
            min_dist = 0.5
            tag = None
            for at in msg.detections:
                if at.transform.translation.z < min_dist:
                    tag = at.tag_id
                    min_dist = at.transform.translation.z

        if tag is None:
            return

        # Wrap transforms in try and except incase the transform is not found
        try:
            # Change LED if required
            for color in self.led_dict:
                if tag in self.led_dict.get(color):
                    break
            self.change_led(color)

            now = rospy.Time.now()
            # Get apriltag transform
            t = self.tfBuffer.lookup_transform('tag/'+str(tag), 'odometry', rospy.Time())
            # Apply previously found transform to the fixed frame
            self.bc.sendTransform(
                [t.transform.translation.x, t.transform.translation.y, t.transform.translation.z],
                [t.transform.rotation.x, t.transform.rotation.y, t.transform.rotation.z,

                 t.transform.rotation.w],
                now, 'predicted_location', 'at_fixed_'+str(tag))
            # Get the previously sent transform in world frame
            t2 = self.tfBuffer.lookup_transform('world', 'predicted_location', now, rospy.Duration(1))
            # Get theta and XYZ, update robots position
            theta = tf.transformations.euler_from_quaternion(
                [t2.transform.rotation.x, t2.transform.rotation.y, t2.transform.rotation.z,
                 t2.transform.rotation.w])
            self.update_pos_client(t2.transform.translation.x, t2.transform.translation.y, 0, float(theta[2]))

        except Exception as e:
            print(e)
            pass

        return


if __name__ == '__main__':
    # create the node
    node = Localization(node_name='localization_node')
    # keep spinning
    rospy.spin()
