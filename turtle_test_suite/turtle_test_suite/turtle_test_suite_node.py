import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtle_test_suite_msgs.msg import Start


class TurtleTestSuite(Node):
    """turtlesim을 제어하는 노드

    움직일 거리를 parameter로 지정하고
    turtle1/start topic에 '1'를 publish시 
    실시간 pose 값과 움직일 거리(parameter) 값을 비교하여
    거리만큼 이동, 도착 시 180도 회전 후 복귀

    Attributes:
        param (float): distance 파라미터의 값
        cmd_vel (:obj:`vector`:`float`): 속도제어 명령 토픽 - linear.(x, y, z) & angular.(x, y, z)
        arrive_pose (:obj:`float`): 도착 할 좌표 토픽 - Pose.(x, y, theta,linear_velocity, angular_velocity)
        arrive_list (list): 도착할 좌표들을 모아놓은 리스트
        arrive_idx (int): arrive_list의 index 용 변수 및 실행 순서 관리

        declare_parameter : distance 파라미터 선언
        subscriber_pose : turtle1/pose 토픽 subscriber
        subscriber_start : turtle1/start 토픽 subscriber
        publisher_cmdvel : turtle1/cmd_vel 토픽 publisher
        timer : 0.1초마다 cmd_vel_callback 메서드 실행
    """

    def __init__(self):
        super().__init__('turtle_test_suite_node')

        self.declare_parameter(
            'distance',
            0.0
        )

        self.param = self.get_parameter('distance').value
        self.cmd_vel = Twist()
        self.arrive_pose = Pose()
        self.arrive_list = []
        self.arrive_idx = 0

        self.subscriber_pose = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10
        )

        self.subscriber_start = self.create_subscription(
            Start,
            'turtle1/start',
            self.start_callback,
            10
        )

        self.publisher_cmdvel = self.create_publisher(
            Twist,
            'turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.cmd_vel_callback
        )

    def start_callback(self, start):
        """subscribe 할 때 start 값 가져오는 메서드

        turtle1/start에 값이 들어오면
        도착할 좌표들을 설정
        """
        if start.data == 1:
            self.arrive_pose.x = self.pose.x + self.param
            self.arrive_pose.theta = self.pose.theta
            self.arrive_list = [
                self.arrive_pose.x,
                self.arrive_pose.theta,
                self.pose.x
            ]
        else:
            self.get_logger().error('Please check the publisher data')

    def pose_callback(self, pose):
        """subscribe 할 때 pose 값 가져오는 메서드

        Args: 
            pose (:obj:`float`): 실시간 좌표와 속도 값 - Pose.(x, y, theta,linear_velocity, angular_velocity)
        Attributes:
            pose (:obj:`float`): pose를 인스턴스 변수에 초기화 - Pose.(x, y, theta,linear_velocity, angular_velocity)
        """
        self.pose = pose

    def cmd_vel_callback(self):
        """publish하는 메서드

        publisher_cmdvel에 self.cmd_vel을 publish
        """
        if self.arrive_list:
            if self.arrive_idx == 0:
                if self.arrive_list[self.arrive_idx] >= self.pose.x:
                    self.cmd_vel.linear.x = 1.0
                    self.cmd_vel.angular.z = 0.0
                else:
                    self.arrive_idx = 1

            elif self.arrive_idx == 1:
                if self.arrive_list[self.arrive_idx] <= self.pose.theta:
                    self.cmd_vel.linear.x = 0.0
                    self.cmd_vel.angular.z = 0.2
                else:
                    self.arrive_idx = 2

            elif self.arrive_idx == 2:
                if self.arrive_list[self.arrive_idx] <= self.pose.x:
                    self.cmd_vel.linear.x = 1.0
                    self.cmd_vel.angular.z = 0.0
                else:
                    self.arrive_idx = 3
            else:
                self.cmd_vel.linear.x = 0.0
                self.cmd_vel.angular.z = 0.0
        else:
            pass

        self.publisher_cmdvel.publish(self.cmd_vel)


def main(args=None):
    """main

    노드를 실행
    """
    rclpy.init(args=args)

    turtle_test_suite_node = TurtleTestSuite()
    try:
        turtle_test_suite_node.get_logger().info(
            'Beginning client, shut down with CTRL-C')
        rclpy.spin(turtle_test_suite_node)
    except KeyboardInterrupt:
        turtle_test_suite_node.get_logger().info(
            'Keyboard interrupt, shutting down.\n')
    turtle_test_suite_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
