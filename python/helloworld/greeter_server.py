# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import time

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        """for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))
        """
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayManyHello(self, request, context):
        for i in range(request.N): 
            time.sleep(1)
            yield helloworld_pb2.HelloReply(message='Hi from stream' + str(i))
        # missing associated documentation comment in .proto file

    def SayManyHello2(self, request, context):
        N=0
        for req in request:
            #time.sleep(1)
            print("read from client -> ", req.name)
            N=N+1
        return helloworld_pb2.HelloReply(message='Hi from SayManyHello2' + str(N))


    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello again from mainex, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
