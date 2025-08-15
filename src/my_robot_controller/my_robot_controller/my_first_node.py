#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node1')
        self.get_logger().info('My first ROS 2 node is running!')

# ERROR: This line should be removed. It's calling rclpy.shutdown() outside of any function,
# which will cause the ROS 2 system to shut down before the node even starts.
rclpy.shutdown()  
'''
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

'''
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()   