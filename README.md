# asyncio-kafka-grpc

This is starting point for putting together the three technologies.

## Architecture

Nothing special. The producer is publishing a single GRPC message in the 'my_topic' topic in Kafka and the consumer is consuming it.

### Kafka
Kafka, Zookeeper and Kafdrop applications using **bitnami** images.

### Consumer
Simple [AIOKafkaConsumer](https://aiokafka.readthedocs.io/en/stable/api.html#aiokafka.AIOKafkaConsumer) that consumes GRPC messages from the 'my_topic' topic of the local Kafka instance.

### Producer
Simple [AIOKafkaProducer](https://aiokafka.readthedocs.io/en/stable/api.html#aiokafka.AIOKafkaProducer) that publishes GRPC messages to the 'my_topic' topic of the local Kafka instance.

### GRPC
GRPC stubs are shared between the consumer and the producer.

## Usage

Make sure you have poetry installed.

Generate the GRPC stubs.

```
cd protos
make grpc-stubs
```

Start Kafka, Zookeeper and Kafdrop using `docker-compose` in the root directory.

```
docker-compose up -d
```

Run the consumer using Makefile.

```
cd python/apps/consumer
poetry install
make run
```

Run the producer using Makefile.
```
python/apps/producer
poetry install
make run
```
