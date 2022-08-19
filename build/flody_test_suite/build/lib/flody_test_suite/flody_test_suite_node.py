import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

from std_msgs.msg import Int16

class FlodyTestSuite(Node):
    def __init__(self):
        super().__init__('flody_test_suite_node')

        #pose subscriber
        self.subscriber_pose = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)

        #start subcriber
        self.subscriber_start = self.create_subscription(
            Int16,
            'turtle1/start',
            self.start_sub_callback,
            10)

        #cmd_vel publisher
        self.publisher_cmdvel = self.create_publisher(
            Twist,
            'turtle1/cmd_vel', 
            10)
        timer_period = 0.1 
        self.timer = self.create_timer(timer_period, self.cmdVel_callback)

        self.pose = Pose()

        self.declare_parameter('distance',0.0)
        self.param =  self.get_parameter('distance').value

    def start_sub_callback(self, start):
        global arrive_pose
        global first_pose

        start = Int16()
        num = Int16()
        num = 1

        if start != num  :
            arrive_pose = Pose()
            first_pose = Pose()
            arrive_pose.x = self.pose.x + self.param
            arrive_pose.theta = 3.14
            first_pose = self.pose
            # self.get_logger().info("param : {0}".format(self.param))    

    def pose_callback(self, pose):
        self.pose = pose

    def cmdVel_callback(self):
        global arrive_pose
        global first_pose

        cmd_vel = Twist()

        #수정해야하는 부분
        try:
            if arrive_pose.x >= self.pose.x :
                cmd_vel.linear.x = 1.0
                self.publisher_cmdvel.publish(cmd_vel)

            elif 3.14 > self.pose.theta :
                cmd_vel.angular.z = 0.1
                self.publisher_cmdvel.publish(cmd_vel)
                arrive_pose.x = first_pose.x

            elif arrive_pose.x < self.pose.x:
                cmd_vel.linear.x = 1.0
                self.publisher_cmdvel.publish(cmd_vel)
            
            else :
                cmd_vel.linear.x = 0.0
                cmd_vel.linear.z = 0.0
                self.publisher_cmdvel.publish(cmd_vel)

        except NameError :
            self.get_logger().info("*pass* x: {0}".format(self.pose.x))
            pass
        
def main(args=None):
    rclpy.init(args=args)

    flody_test_suite = FlodyTestSuite()

    rclpy.spin(flody_test_suite)

    flody_test_suite.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()