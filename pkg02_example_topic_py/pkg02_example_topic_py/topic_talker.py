import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class node_publisher(Node):
	def __init__(self, name):
		super().__init__(name)
		self.get_logger().info(f'node {name} init!')
		self.publisher = self.create_publisher(String, 'topic', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		msg = String()
		msg.data = f'msg : {self.i}'
		self.publisher.publish(msg)
		self.get_logger().info(f'talker : {msg.data}')
		self.i += 1

def main(args=None):
	rclpy.init(args=args)
	node = node_publisher('node_talke')
	rclpy.spin(node)

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
    main()
