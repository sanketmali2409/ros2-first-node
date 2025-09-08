import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class YesNoClient(Node):
    def __init__(self):
        super().__init__("yes_no_client")
        self.cli = self.create_client(SetBool, "yes_no_service")

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Service not available, waiting...")

    def send_request(self, user_input: str):
        req = SetBool.Request()
        req.data = (user_input.lower() == "yes")
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    node = YesNoClient()

    while True:
        user_input = input("👉 Enter Yes or No (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting client...")
            break

        if user_input.lower() not in ["yes", "no"]:
            print("⚠️ Please type only 'Yes' or 'No'")
            continue

        response = node.send_request(user_input)
        print(f"🔹 Service Response: {response.message}")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
