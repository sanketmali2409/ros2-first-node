#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class LEDClient(Node):
    def __init__(self):
        super().__init__('led_client')
        self.client = self.create_client(SetBool, 'led_control')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        
        # Send request to turn LED ON
        request = SetBool.Request()
        request.data = True  # True = ON, False = OFF
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f"Service response: {future.result().message}")
        else:
            self.get_logger().error("Service call failed")

def main(args=None):
    rclpy.init(args=args)
    node = LEDClient()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
