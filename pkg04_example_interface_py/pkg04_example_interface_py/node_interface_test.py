import rclpy
from rclpy.node import Node

from interfaces01_test.msg import Num


class MinimalSubscriber(Node):

    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info(f'node {name} init!')
        self.subscription = self.create_subscription(
            Num,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, num):
        self.get_logger().info(f'I heard: "{num}"')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber('node_listen')

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

