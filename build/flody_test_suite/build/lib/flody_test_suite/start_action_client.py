import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from msg_srv_action_interface_example.action import TurtleStart


class StartActionClient(Node):

    def __init__(self):
        super().__init__('start_action_client')
        self._action_client = ActionClient(
            self,
            TurtleStart,
            'turtlestart')

    def send_goal(self, order):
        goal_msg = TurtleStart.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.goal))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.pose))

def main(args=None):
    rclpy.init(args=args)

    start_action_client = StartActionClient()

    future = start_action_client.send_goal('go')

    rclpy.spin(start_action_client)


if __name__ == '__main__':
    main()