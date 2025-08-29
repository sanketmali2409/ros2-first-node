#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool  # Standard ROS 2 service: request boolean, reply boolean+message

class LEDService(Node):
    def __init__(self):
        super().__init__('led_service')
        self.srv = self.create_service(SetBool, 'led_control', self.led_callback)

    def led_callback(self, request, response):
        if request.data:  


            
            response.success = True
            response.message = "LED turned ON"
        else:
            response.success = True
            response.message = "LED turned OFF"
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LEDService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
