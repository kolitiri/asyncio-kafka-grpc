from typing import List

from aiokafka import AIOKafkaConsumer


class KafkaConsumer:
	""" Async context manager for opening/closing a connection
		to a kafka broker and returning a kafka consumer client.
	"""
	def __init__(
		self,
		bootstrap_servers: List[str],
		topic: str,
	):
		self.kafka_client = AIOKafkaConsumer(
			topic,
			bootstrap_servers=bootstrap_servers,
		)

	async def __aenter__(self) -> AIOKafkaConsumer:
		try:
			await self.kafka_client.start()
		except Exception as exc:
			await self.kafka_client.stop()
			raise exc

		return self.kafka_client

	async def __aexit__(self, type, value, traceback):
		await self.kafka_client.stop()
