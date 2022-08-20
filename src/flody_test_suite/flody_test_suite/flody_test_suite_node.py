import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.exceptions import ParameterNotDeclaredException

from msg_srv_action_interface_example.action import TurtleStart
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16

class FlodyTestSuite(Node):

    arrive_pose = Pose()

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

        self.declare_parameter('distance',0.0)
        self.param =  self.get_parameter('distance').value
        # self.get_logger().info('param: {0}'.format(self.param))

    def start_act_callback(self, goal_handle):
        self.get_logger().info('Excuting goal...')

        feedback_msg = TurtleStart.Feedback()
        feedback_msg.pose = self.pose.x
        
        if goal_handle.request.order == "go":
            FlodyTestSuite.arrive_pose.x = self.pose.x + self.param
            FlodyTestSuite.arrive_pose.theta = 3.14059265359
            
            # self.get_logger().info('arrive_pose.x: {0} pose.x: {0} parm: {0}'.format(FlodyTestSuite.arrive_pose.x,self.pose.x,self.param))

            self.get_logger().info('Feedback: {0}'.format(feedback_msg.pose))
            goal_handle.publish_feedback(feedback_msg)

        else :
            self.get_logger().info('please check the data..')

        goal_handle.succeed()
        result = TurtleStart.Result()
        result.goal = feedback_msg.pose
        return result
        
    def pose_callback(self, pose):
        self.pose = pose

    def cmdVel_callback(self):
        cmd_vel = Twist()

        #수정해야하는 부분들 
        if FlodyTestSuite.arrive_pose.x >= self.pose.x :
            cmd_vel.linear.x = 0.1
            self.publisher_cmdvel.publish(cmd_vel) 

        # if FlodyTestSuite.arrive_pose.theta >= self.pose.theta : 
        #     cmd_vel.angular.z = 0.01
        #     self.publisher_cmdvel.publish(cmd_vel)
        
        else :
            cmd_vel.linear.x = 0.0
            cmd_vel.linear.z = 0.0
            self.publisher_cmdvel.publish(cmd_vel)
        
def main(args=None):
    rclpy.init(args=args)
    
    flody_test_suite = FlodyTestSuite()

    rclpy.spin(flody_test_suite)

    flody_test_suite.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()