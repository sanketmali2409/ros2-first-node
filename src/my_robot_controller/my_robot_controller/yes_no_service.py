import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class YesNoService(Node):
    def __init__(self):
        super().__init__("yes_no_service")
        self.srv = self.create_service(SetBool, "yes_no_service", self.callback)
        self.get_logger().info("✅ Yes/No Service is ready...")

    def callback(self, request, response):
        if request.data:  # True = yes
            response.success = True
            response.message = "You said YES 👍"
        else:  # False = no
            response.success = True
            response.message = "You said NO 👎"

        self.get_logger().info(f"➡️ Service received: {response.message}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = YesNoService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
