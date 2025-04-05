import time
from concurrent import futures

import grpc

import node_pb2
import node_pb2_grpc


class NodeServiceServicer(node_pb2_grpc.NodeServiceServicer):
    def CheckNode(self, request, context):
        is_available = True
        message = "Destination node is available"
        print("Received a CheckNode request.")
        return node_pb2.CheckResponse(available=is_available, message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    node_pb2_grpc.add_NodeServiceServicer_to_server(NodeServiceServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Destination gRPC server is running on port 50051...")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
