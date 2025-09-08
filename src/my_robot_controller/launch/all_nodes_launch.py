#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Publisher Node
        Node(
            package='my_robot_controller',
            executable='publisher_node',
            name='publisher_node'
        ),

        # Subscriber Node
        Node(
            package='my_robot_controller',
            executable='subscriber_node',
            name='subscriber_node'
        ),

        # Service Node
        Node(
            package='my_robot_controller',
            executable='service_node',
            name='service_node'
        ),

        # Client Node
        Node(
            package='my_robot_controller',
            executable='client_node',
            name='client_node'
        ),
          Node(
            package='my_robot_controller',
            executable='led_client',
            name='led_client'
        ),
          Node(
            package='my_robot_controller',
            executable='led_service',
            name='led_service'
        ),
        Node(
            package='my_robot_controller',
            executable='yes_no_service',
            name='yes_no_service'
        ),
        Node(
            package='my_robot_controller',
            executable='yes_no_client',
            name='yes_no_client'
        ),
    ])
