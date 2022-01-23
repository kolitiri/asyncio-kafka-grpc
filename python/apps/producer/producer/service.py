from contextlib import AsyncExitStack
from datetime import datetime

from google.protobuf.message import Message as ProtoBufMessage
from google.protobuf.struct_pb2 import Struct
from google.protobuf.timestamp_pb2 import Timestamp

from grpc_stubs.kafkacomms.producer_pb2 import SampleMsg
from producer.exceptions import NotSerialisable
from producer.kafka import KafkaProducer


BOOTSTRAP_SERVERS = ['127.0.0.1:9092']

def serialise(msg: ProtoBufMessage) -> bytes:
	""" Serialises a protobuf message """
	if not isinstance(msg, ProtoBufMessage):
		raise NotSerialisable()
	return msg.SerializeToString()


async def run() -> None:
	async with AsyncExitStack() as stack:

		# Create a Kafka producer client
		print(f"Running Kafka producer at: {BOOTSTRAP_SERVERS}")

		kafka_producer = await stack.enter_async_context(
			KafkaProducer(
				max_request_size=10000,
				bootstrap_servers=BOOTSTRAP_SERVERS,
				request_timeout_ms=10000,
			)
		)

		# Create a GRPC message
		msg_other_data = Struct()
		msg_other_data.update({
			'key_1': 'val_1',
			'key_2': 'val_2',
		})

		kafka_grpc_msg = SampleMsg(
			msg_no=1,
			msg_body='my text',
			msg_date=Timestamp(),
			msg_other_data=msg_other_data,
		)

		# Send the message to the Kafka broker
		await kafka_producer.send_and_wait(
			'my_topic',
			value=serialise(kafka_grpc_msg),
			key=bytes('my_key', 'utf-8'),
			headers=[
				('my_header_name', b'my_header_value')
			],
		)

		print(f"Sent message: {kafka_grpc_msg}")
