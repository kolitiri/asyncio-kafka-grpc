from contextlib import AsyncExitStack

from consumer.kafka import KafkaConsumer
from grpc_stubs.kafkacomms.producer_pb2 import SampleMsg


BOOTSTRAP_SERVERS = ['127.0.0.1:9092']

def deserialize(msg: bytes) -> SampleMsg:
	""" Deserialises to a protobuf message """
	deserialized_msg = SampleMsg()
	deserialized_msg.ParseFromString(msg)
	return deserialized_msg


async def run() -> None:
	async with AsyncExitStack() as stack:

		# Create a Kafka consumer client
		print(f"Running Kafka consumer at: {BOOTSTRAP_SERVERS}")

		kafka_consumer = await stack.enter_async_context(
			KafkaConsumer(
				topic='my_topic',
				bootstrap_servers=BOOTSTRAP_SERVERS,
			)
		)

		# Start consuming messages from the topic
		async for msg in kafka_consumer:
			print(f"Received msg: {deserialize(msg.value)}")
