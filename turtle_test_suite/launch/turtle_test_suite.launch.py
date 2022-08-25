import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('turtle_test_suite'),
        'config',
        'params.yaml'
    )

    turtle_test_suite_node = Node(
        package="turtle_test_suite",
        executable="turtle_test_suite_node",
        parameters=[config]
    )

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    ld.add_action(turtle_test_suite_node)
    ld.add_action(turtlesim_node)

    return ld
