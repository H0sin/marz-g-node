import asyncio
import time
from concurrent import futures

import grpc

import node_pb2
import node_pb2_grpc
from credentials import load_tls_credentials


class NodeServiceServicer(node_pb2_grpc.NodeServiceServicer):
    def CheckNode(self, request, context):
        is_available = True
        message = "Destination node is available"
        print("Received a CheckNode request.")
        return node_pb2.CheckResponse(available=is_available, message=message)


def serve():
    private_key, certificate_chain = asyncio.run(load_tls_credentials())

    server_credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)]
    )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    node_pb2_grpc.add_NodeServiceServicer_to_server(NodeServiceServicer(), server)

    server.add_secure_port('[::]:50051', server_credentials)

    print("✅ gRPC server started with TLS on port 50051")
    server.start()

    server.wait_for_termination()


if __name__ == '__main__':
    serve()
