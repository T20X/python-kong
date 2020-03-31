# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/helloworld.Greeter/SayHello',
        request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
        response_deserializer=helloworld__pb2.HelloReply.FromString,
        )
    self.SayManyHello = channel.unary_stream(
        '/helloworld.Greeter/SayManyHello',
        request_serializer=helloworld__pb2.StreamRequest.SerializeToString,
        response_deserializer=helloworld__pb2.HelloReply.FromString,
        )
    self.SayManyHello2 = channel.stream_unary(
        '/helloworld.Greeter/SayManyHello2',
        request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
        response_deserializer=helloworld__pb2.HelloReply.FromString,
        )
    self.SayHelloAgain = channel.unary_unary(
        '/helloworld.Greeter/SayHelloAgain',
        request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
        response_deserializer=helloworld__pb2.HelloReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayManyHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayManyHello2(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloAgain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=helloworld__pb2.HelloRequest.FromString,
          response_serializer=helloworld__pb2.HelloReply.SerializeToString,
      ),
      'SayManyHello': grpc.unary_stream_rpc_method_handler(
          servicer.SayManyHello,
          request_deserializer=helloworld__pb2.StreamRequest.FromString,
          response_serializer=helloworld__pb2.HelloReply.SerializeToString,
      ),
      'SayManyHello2': grpc.stream_unary_rpc_method_handler(
          servicer.SayManyHello2,
          request_deserializer=helloworld__pb2.HelloRequest.FromString,
          response_serializer=helloworld__pb2.HelloReply.SerializeToString,
      ),
      'SayHelloAgain': grpc.unary_unary_rpc_method_handler(
          servicer.SayHelloAgain,
          request_deserializer=helloworld__pb2.HelloRequest.FromString,
          response_serializer=helloworld__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
