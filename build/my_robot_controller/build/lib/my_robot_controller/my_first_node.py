#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node1')
        self.get_logger().info('My first ROS 2 node is running!')

def main(args=None):
    rclpy.init(args=args)         # Initialize ROS
    node = MyNode()               # Create node
    rclpy.spin(node)              # Keep it running
    node.destroy_node()           # Cleanup node
    rclpy.shutdown()              # Shutdown ROS

if __name__ == '__main__':
    main()

  