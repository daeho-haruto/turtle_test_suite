import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose

class PoseSub(Node):

    def __init__(self):
        super().__init__('pose_sub')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, pose):
        self.get_logger().info('x: {0} y: {0}'.format(pose.x, pose.y))

def main(args=None):
    rclpy.init(args=args)

    pose_sub = PoseSub()

    rclpy.spin_once(pose_sub)

    pose_sub.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
