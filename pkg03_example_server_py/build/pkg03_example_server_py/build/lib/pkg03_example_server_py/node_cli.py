import sys
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class node_client(Node):
	def __init__(self, name):
		# 调用node初始化
		super().__init__(name)
		# logo
		self.get_logger().info(f'node {name} init!')
		# 创建客户端
		self.cli = self.create_client(AddTwoInts, 'add_two_ints')
		# 检测服务端
		while not self.cli.wait_for_service(timeout_sec = 1.0):
			self.get_logger().info(f'service no available, wait again ....')
		# 定义req结构体变量
		self.req = AddTwoInts.Request()

	def send_request(self):
		self.req.a = int(sys.argv[1])
		self.req.b = int(sys.argv[2])
		self.future = self.cli.call_async(self.req)

def main(args=None):
	rclpy.init(args=args)
	node = node_client('node_cli')
	node.send_request()

	while rclpy.ok():
		rcply.spin_once(node)
		if node.future.done():
			try:
				response = node.future.result()
			except Exception as e:
				node.get_logger().info(f'server call fail {e,}')
			else:
				node.get_logger().info(
					f'result of add_two_ints : for {node.req.a} + {node.req.b} = {responce.sum}')
			break

	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
    main()
