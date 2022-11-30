from kafka import KafkaProducer
import grpc
import item_pb2
import item_pb2_grpc
import logging
from concurrent import futures

producer = KafkaProducer(bootstrap_servers='kafka-release.default.svc.cluster.local:9092')

class ItemServicer(item_pb2_grpc.ItemServiceServicer):
    def Create(self, request, context):
        request_value= {
            "person_id":int(request.person_id),
            "latitude":int(request.latitude),
            "longitude":int(request.longitude)
        }
        print(request_value)
        return item_pb2.ItemMessage(**request_value)
        

def publish_message(message):
    request = json.dumps(message).encode()
    producer.send('test', request)
    producer.flush()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)
    server.add_insecure_port("[::]:5005")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
