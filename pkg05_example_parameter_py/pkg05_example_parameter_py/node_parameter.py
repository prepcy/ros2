import rclpy
from rclpy.node import Node

class node_parameter(Node):
	def __init__(self, name):
		super().__init__(name)
		self.get_logger().info(f'node {name} init!')
		timer_period = 2
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.declare_parameter('parameter_test', 'test')

	def timer_callback(self):
		my_param = self.get_parameter('parameter_test').get_parameter_value().string_value
		self.get_logger().info(f'node parameter : {my_param}')

		my_new_param = rclpy.parameter.Parameter(
			'parameter_test',
			rclpy.Parameter.Type.STRING,
			'test'
		)
		all_new_parameters = [my_new_param]
		self.set_parameters(all_new_parameters)

def main(args=None):
	rclpy.init(args=args)
	node = node_parameter('node_param')
	rclpy.spin(node)

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
    main()
