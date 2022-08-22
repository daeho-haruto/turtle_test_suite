import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from turtlesim.msg import Pose
from msg_srv_action_interface_example.action import TurtleStart

class CallbackGroupDemo(Node):
    def __init__(self):
        super().__init__('action_server_node')
        
        sub_cb_group = MutuallyExclusiveCallbackGroup()
        act_cb_group = None

        self.subscriber_pose = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10,
            callback_group=sub_cb_group)

        self._action_server = ActionServer(
            self,
            TurtleStart,
            'turtlestart',
            self.start_act_callback,
            callback_group=act_cb_group)

    def pose_callback(self, pose):
        self.pose = pose
        # self.get_logger().info('pose: {0}'.format(self.pose))
        
    def start_act_callback(self, goal_handle):
        self.get_logger().info('Excuting goal...')

        feedback_msg = TurtleStart.Feedback()
        feedback_msg.pose = self.pose.x

        if goal_handle.request.order == "go":
            while 10 >= feedback_msg.pose :
                self.get_logger().info('pose: {0}'.format(self.pose))
                goal_handle.publish_feedback(feedback_msg)

            goal_handle.succeed()
            result = TurtleStart.Result()
            result.goal = feedback_msg.pose
            return result

        else :
            self.get_logger().info('please check the data..')

        # goal_handle.succeed()
        # result = TurtleStart.Result()
        # result.goal = feedback_msg.pose
        # return result

def main(args=None):
    rclpy.init(args=args)
    
    node = CallbackGroupDemo()
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