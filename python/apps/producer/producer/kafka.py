from typing import List

from aiokafka import AIOKafkaProducer


class KafkaProducer:
	""" Async context manager for opening/closing a connection
		to a kafka broker and returning a kafka producer client.
	"""
	def __init__(
		self,
		bootstrap_servers: List[str],
		max_request_size: int,
		request_timeout_ms: int,
	):
		self.kafka_client = AIOKafkaProducer(
			bootstrap_servers=bootstrap_servers,
			max_request_size=max_request_size,
			request_timeout_ms=request_timeout_ms,
		)

	async def __aenter__(self) -> AIOKafkaProducer:
		try:
			await self.kafka_client.start()
		except Exception as exc:
			await self.kafka_client.stop()
			raise exc

		return self.kafka_client

	async def __aexit__(self, type, value, traceback):
		await self.kafka_client.stop()
