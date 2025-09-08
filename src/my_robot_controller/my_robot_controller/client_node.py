#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

        request = AddTwoInts.Request()
        request.a = 7
        request.b = 5

        self.future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            self.get_logger().info(f"Result: {request.a} + {request.b} = {self.future.result().sum}")
        else:
            self.get_logger().error("Service call failed")

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
