class NotSerialisable(Exception):
	""" Raised when we attempt to serialise a non protobuf message """
	def __init__(self):
		self.message = "Can only serialise protobuf objects"
		super().__init__(self.message)
