import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from interfaces01_test.action import Fibonacci


class node_action_clent(Node):
	def __init__(self, name):
		super().__init__(name)
		self.get_logger().info(f'node {name} init!')
		self.action_client = ActionClient(self, Fibonacci,'fibonacci')

	def send_goal(self, order):
		self.get_logger().info(f'send order: {order}')
		goal_msg = Fibonacci.Goal()
		goal_msg.order = order

		self.action_client.wait_for_server()
		self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
		self.send_goal_future.add_done_callback(self.goal_response_callback)

	def goal_response_callback(self, future):
		goal_handle = future.result()
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return

		self.get_logger().info('Goal accepted :)')

		self.get_result_future = goal_handle.get_result_async()
		self.get_result_future.add_done_callback(self.get_result_callback)

	def get_result_callback(self, future):
		result = future.result().result
		self.get_logger().info('Result: {0}'.format(result.sequence))
		rclpy.shutdown()

	def feedback_callback(self, feedback_msg):
		feedback = feedback_msg.feedback
		self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))

def main(args=None):
	rclpy.init(args=args)
	node = node_action_clent('node_action_client')

	node.send_goal(10)
	rclpy.spin(node)

	#node.destroy_node()


if __name__ == '__main__':
	main()

