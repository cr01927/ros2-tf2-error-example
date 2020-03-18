import tf2_py
import tf2_ros

import rclpy
from rclpy.logging import get_logger
from rclpy.node import Node
from rclpy.qos import QoSPresetProfiles, QoSProfile, QoSDurabilityPolicy

import std_msgs.msg as std_msgs

class TestNodeListener(Node):

    def __init__(self):
        super().__init__("test_node")

        self.create_subscription(std_msgs.Empty, "topic_tl", self.on_topic_tl, qos_profile=QoSProfile(
            depth=1,
            durability=QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL,
            )
        )

        self.create_subscription(std_msgs.Empty, "topic_normal", self.on_topic_normal, qos_profile=QoSPresetProfiles.SERVICES_DEFAULT.value
        )

        self._buffer = tf2_ros.Buffer()
        self._listener = tf2_ros.TransformListener(
                self._buffer, self, spin_thread=True
        )
        get_logger(__name__).info("Initialized")

    def on_topic_tl(self, msg):
        get_logger(__name__).info("Received on 'topic_tl'")

    def on_topic_normal(self, msg):
        get_logger(__name__).info("Received on 'topic_normal'")


class TestNodeTalker(Node):

    def __init__(self):
        super().__init__("test_node_listener")

        self.topic_tl_pub = self.create_publisher(std_msgs.Empty, "topic_tl", qos_profile=QoSProfile(
            depth=1,
            durability=QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL,
            )
        )

        self.topic_normal_pub = self.create_publisher(std_msgs.Empty, "topic_normal", qos_profile=QoSPresetProfiles.SERVICES_DEFAULT.value
        )

        self.create_timer(5, self.publish_both)

    def publish_both(self):
        get_logger(__name__).info("Publishing")
        self.topic_tl_pub.publish(std_msgs.Empty())
        self.topic_normal_pub.publish(std_msgs.Empty())

def listener_main():
    rclpy.init()
    node = TestNodeListener()
    rclpy.spin(node)

def talker_main():
    rclpy.init()
    node = TestNodeTalker()
    rclpy.spin(node)
