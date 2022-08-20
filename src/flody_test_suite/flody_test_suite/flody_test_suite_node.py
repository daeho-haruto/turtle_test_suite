import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.exceptions import ParameterNotDeclaredException

from msg_srv_action_interface_example.action import TurtleStart
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
        
        #action server
        self._action_server = ActionServer(
            self,
            TurtleStart,
            'turtlestart',
            self.start_act_callback)

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

    def start_act_callback(self, goal_handle):
        self.get_logger().info('Excuting goal...')

        #test code - 글로벌 없애는 작업에서 수정예정
        feedback_msg = TurtleStart.Feedback()
        feedback_msg.pose = 0.0

        if goal_handle.request.order == "go":
            for i in range(0, 5):
                feedback_msg.pose = feedback_msg.pose + 1
                self.get_logger().info('Feedback: {0}'.format(feedback_msg.pose))
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(1)

            goal_handle.succeed()
        else :
            self.get_logger().info('please check the data..')

        result = TurtleStart.Result()
        result.goal = feedback_msg.pose
        return result


        
    def pose_callback(self, pose):
        self.pose = pose

    def cmdVel_callback(self):
        global arrive_pose
        global first_pose

        cmd_vel = Twist()

        #수정해야하는 부분들 
        try:
            if arrive_pose.x >= self.pose.x :
                cmd_vel.linear.x = 1.0
                self.publisher_cmdvel.publish(cmd_vel) 

            #3.14에 최대한 근접한 값으로 만들어아 함
            elif 3.14 > self.pose.theta : 
                cmd_vel.angular.z = 0.1
                self.publisher_cmdvel.publish(cmd_vel)
                arrive_pose.x = first_pose.x
            
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