import time 
import json 
from concurrent import futures

import grpc 
import item_pb2
import item_pb2_grpc
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='kafka-release.default.svc.cluster.local:9092')


class ItemService(item_pb2_grpc.ItemService):
    def Create(self, request, context):

        request_ = {
            'user_id': request.user_id,
            'latitude': request.latitude,
            'longitude': request.longitude,
        }
        print(request_)
        message = json.dumps(request_, indent=2).encode('utf-8')
        producer.send('test', message)
        return item_pb2.itemMessage(**request_)

port = f'[::]:50005'
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)
print('Server available local:50005...')
server.add_insecure_port(port)
server.start()
try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    server.stop(0)