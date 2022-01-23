PYTHON_OUT=../python/common/grpc_stubs/src/grpc_stubs/

grpc-stubs:
	@poetry run python -m grpc_tools.protoc -I. \
		--python_out=$(PYTHON_OUT) \
		--grpc_python_out=$(PYTHON_OUT) \
		./kafkacomms/*.proto

delete-grpc-stubs:
	find ../python/common/grpc_stubs/src/grpc_stubs/kafkacomms/ -path "*pb2*" | xargs rm

.PHONY: grpc-stubs
