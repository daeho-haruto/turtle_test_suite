import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class Cmd_velPub(Node):
    def __init__(self):
        super().__init__('cmd_vel_pub')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.num = self.get_parameter('distance').value #param

    def timer_callback(self):
        cmd_vel = Twist()
        cmd_vel.linear = self.num
        self.publisher_.publish(cmd_vel)
        # self.get_logger().info("linear : {0}".foramt(cmd_vel.linear))

def main(args=None):
    rclpy.init(args=args)

    cmd_vel_pub = Cmd_velPub()

    rclpy.spin_once(cmd_vel_pub)

    cmd_vel_pub.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
