import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from msg_srv_action_interface_example.action import TurtleStart

class StartActionServer(Node):  
    def __init__(self):
        super().__init__('start_action_server')
        self._action_server = ActionServer(
            self,
            TurtleStart,
            'turtlestart',
            self.start_act_callback)
        
    def start_act_callback(self, goal_handle):
        self.get_logger().info('Excuting goal...')

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


def main(args=None):
    rclpy.init(args=args)

    start_action_server = StartActionServer()

    rclpy.spin(start_action_server)

if __name__ == '__main__':
    main()