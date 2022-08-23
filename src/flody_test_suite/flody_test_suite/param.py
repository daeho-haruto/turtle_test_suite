import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException

class TestParams(Node):

    def __init__(self):
        super().__init__('test_params')

        self.declare_parameters(
            namespace='',
            parameters=[
                ('distance', 0)
            ]
        )

def main(args=None):
    rclpy.init(args=args)

    node = TestParams()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()