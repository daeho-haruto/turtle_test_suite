import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor

from msg_srv_action_interface_example.action import TurtleStart
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class TurtleTestSuite(Node):
    """turtlesim을 제어하는 노드

    움직일 거리를 parameter로 지정하고
    action goal 값에 'go'를 입력 시
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
        start_action_server : turtlestart의 action server
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

        self.start_action_server = ActionServer(
            self,
            TurtleStart,
            'turtlestart',
            self.start_action_callback
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

    def start_action_callback(self, goal_handle):
        """액션 값이 들어오면 실행되는 메서드

        turtlestart 액션에 값이 들어오면
        도착할 좌표들을 설정 후 cmd_vel 값 초기화 

        Args: 
            goal_handle (string): 액션 처리 객체

        Attributes:
            feedback_msg (:obj:`float`): 피드백 값을 관리한다. - Feedback.(x, y, theta)
            result (:obj:`float`): 액션 result 값 초기화

        Returns:
            result (:obj:`float`): 도착 pose.x 값 리턴
        """
        self.get_logger().info('Excuting goal...')

        feedback_msg = TurtleStart.Feedback()

        if goal_handle.request.order == "go":
            self.arrive_pose.x = self.pose.x + self.param
            self.arrive_pose.theta = self.pose.theta
            self.arrive_list = [
                self.arrive_pose.x,
                self.arrive_pose.theta,
                self.pose.x
            ]

            while True:
                if self.arrive_idx == 3:
                    break

                feedback_msg.x = self.pose.x
                feedback_msg.y = self.pose.y
                feedback_msg.theta = self.pose.theta

                self.get_logger().info('x: {0} y: {1} theta: {2}'.format(
                    feedback_msg.x, feedback_msg.y, feedback_msg.theta))

                if self.arrive_list:
                    if self.arrive_idx == 0:
                        if self.arrive_list[self.arrive_idx] >= feedback_msg.x:
                            self.cmd_vel.linear.x = 1.0
                            self.cmd_vel.angular.z = 0.0
                        else:
                            self.arrive_idx = 1

                    elif self.arrive_idx == 1:
                        if self.arrive_list[self.arrive_idx] <= feedback_msg.theta:
                            self.cmd_vel.linear.x = 0.0
                            self.cmd_vel.angular.z = 0.1
                        else:
                            self.arrive_idx = 2

                    elif self.arrive_idx == 2:
                        if self.arrive_list[self.arrive_idx] <= feedback_msg.x:
                            self.cmd_vel.linear.x = 1.0
                            self.cmd_vel.angular.z = 0.0
                        else:
                            self.arrive_idx = 3
                else:
                    pass

                goal_handle.publish_feedback(feedback_msg)  # 피드백 값 발행

            feedback_msg.x = self.pose.x
            self.cmd_vel.linear.x = 0.0
            self.cmd_vel.angular.z = 0.0

            goal_handle.succeed()
            result = TurtleStart.Result()
            result.goal = feedback_msg.x
            return result

        else:
            self.get_logger().info('please check the data..')

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

        publisher_cmdvel에 self.cmd_vel을 publish합니다.
        """
        self.publisher_cmdvel.publish(self.cmd_vel)


def main(args=None):
    """main 
    
    Attributes:
        excutor : 노드를 멀티 스레딩 하게 해준다.
    """
    rclpy.init(args=args)

    turtle_test_suite_node = TurtleTestSuite()
    executor = MultiThreadedExecutor()
    executor.add_node(turtle_test_suite_node)

    try:
        turtle_test_suite_node.get_logger().info(
            'Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        turtle_test_suite_node.get_logger().info(
            'Keyboard interrupt, shutting down.\n')
    turtle_test_suite_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
