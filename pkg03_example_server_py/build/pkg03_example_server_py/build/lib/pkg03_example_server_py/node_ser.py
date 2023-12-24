import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class node_server(Node):
	def __init__(self, name):
		super().__init__(name)
		self.get_logger().info(f'node {name} init!')
		self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

	def add_two_ints_callback(self, request, response):
		response.sum = request.a + request.b
		self.get_logger().info(f'Incoming request\na: {request.a} b: {request.b}')

		return response

def main(args=None):
	rclpy.init(args=args)
	node = node_server('node_ser')
	rclpy.spin(node)

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
    main()
