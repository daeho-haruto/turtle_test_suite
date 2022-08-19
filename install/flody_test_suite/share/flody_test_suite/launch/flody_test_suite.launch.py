import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('flody_test_suite'),
        'config',
        'params.yaml'
    )

    print(config)

    flody_test_suite_node = Node(
        package="flody_test_suite",
        executable="flody_test_suite_node",
        parameters=[
            config
        ]
    )

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    ld.add_action(flody_test_suite_node)
    ld.add_action(turtlesim_node)

    return ld
