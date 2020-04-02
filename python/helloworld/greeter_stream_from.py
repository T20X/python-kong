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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc
import datetime 

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('192.168.56.7:9080', options=[
        ('grpc.keepalive_time_ms', 10000),
        ('grpc.keepalive_timeout_ms', 5000),
        ('grpc.keepalive_permit_without_calls', True)
      ]) as channel: 
        a = datetime.datetime.now()
        N=0
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        for response in stub.SayManyHello(helloworld_pb2.StreamRequest(N=100), metadata = (('authorization', 'LDAP SHViZXJ0IEouIEZhcm5zd29ydGgsb3U9cGVvcGxlOnByb2Zlc3Nvcg=='), )):
            print("Greeter client received: " + response.message)
            N=N+1 

        b = datetime.datetime.now()
        print("Perf is:", ((b-a).total_seconds()/N)*1000, " ms per call")

        """ response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
         """

if __name__ == '__main__':
    logging.basicConfig()
    run()
