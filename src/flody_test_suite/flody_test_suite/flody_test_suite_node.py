import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.exceptions import ParameterNotDeclaredException
from rclpy.executors import MultiThreadedExecutor

from msg_srv_action_interface_example.action import TurtleStart
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class FlodyTestSuite(Node):

    arrive_pose = Pose()
    arrive_list = []
    arrive_idx = 0

    def __init__(self):
        super().__init__('flody_test_suite_node')

        self.declare_parameter('distance',0.0)
        self.param =  self.get_parameter('distance').value

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
        self.timer = self.create_timer(0.1, self.cmdVel_callback)

    def start_act_callback(self, goal_handle):
        self.get_logger().info('Excuting goal...')

        feedback_msg = TurtleStart.Feedback()
        
        if goal_handle.request.order == "go":
            # !!!
            FlodyTestSuite.arrive_pose.x = self.pose.x + self.param
            FlodyTestSuite.arrive_pose.theta = self.pose.theta 
            FlodyTestSuite.arrive_list = [FlodyTestSuite.arrive_pose.x, FlodyTestSuite.arrive_pose.theta, self.pose.x]
            
            while True: 
                if FlodyTestSuite.arrive_idx == 3:
                    break
                feedback_msg.pose = self.pose.x
                # self.get_logger().info('arrive_pose.x: {0} pose.x: {1} param: {2}'.format(FlodyTestSuite.arrive_pose.x,self.pose.x,self.param))
                self.get_logger().info('Feedback: {0}'.format(feedback_msg.pose))
                
                goal_handle.publish_feedback(feedback_msg)

            # self.get_logger().info('pose: {0}'.format(self.pose.x))

            feedback_msg.pose = self.pose.x

            goal_handle.succeed()
            result = TurtleStart.Result()
            result.goal = feedback_msg.pose
            return result

        else :
            self.get_logger().info('please check the data..')

    def pose_callback(self, pose):
        self.pose = pose

    def cmdVel_callback(self):
        cmd_vel = Twist()
        if FlodyTestSuite.arrive_list:
            if FlodyTestSuite.arrive_idx == 0 :
                if FlodyTestSuite.arrive_list[FlodyTestSuite.arrive_idx] >= self.pose.x :
                    cmd_vel.linear.x = 1.0
                else: FlodyTestSuite.arrive_idx = 1

            elif FlodyTestSuite.arrive_idx == 1 :
                if  FlodyTestSuite.arrive_list[FlodyTestSuite.arrive_idx] <= self.pose.theta :
                    cmd_vel.angular.z = 0.1
                else: FlodyTestSuite.arrive_idx = 2

            elif FlodyTestSuite.arrive_idx == 2 :
                if FlodyTestSuite.arrive_list[FlodyTestSuite.arrive_idx] <= self.pose.x : 
                    cmd_vel.linear.x = 1.0
                else: FlodyTestSuite.arrive_idx = 3
        else:
            pass

        self.publisher_cmdvel.publish(cmd_vel)

        
def main(args=None):
    rclpy.init(args=args)

    node = FlodyTestSuite()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        node.get_logger().info('Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()