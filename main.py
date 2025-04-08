import asyncio
from concurrent import futures
import grpc

import node_pb2
import node_pb2_grpc
from credentials import load_tls_credentials


class NodeServiceServicer(node_pb2_grpc.NodeServiceServicer):
    def CheckNode(self, request, context):
        print("✅ Received a CheckNode request")
        return node_pb2.CheckResponse(
            available=True,
            message="Node is available via TLS"
        )


def serve():
    private_key, certificate_chain = asyncio.run(load_tls_credentials())

    server_credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)],
        root_certificates=None,
        require_client_auth=False
    )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    node_pb2_grpc.add_NodeServiceServicer_to_server(NodeServiceServicer(), server)
    server.add_secure_port('[::]:50051', server_credentials)

    print("\U0001F680 gRPC server started with TLS on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
