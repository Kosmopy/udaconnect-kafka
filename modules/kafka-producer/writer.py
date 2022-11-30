import grpc
import item_pb2
import item_pb2_grpc
import logging

print ("Sending location data...")
channel = grpc.insecure_channel("localhost:30005")
stub = item_pb2_grpc.ItemServiceStub(channel)


item= item_pb2.ItemMessage(
        person_id=1,
        latitude=50,
        longitude=10)

response= stub.Create(item)

print(
    "Location of user: "
    + str(response.person_id)
    + ", Lat:"
    + str(response.latitude)
    + ", Long:"
    + str(response.longitude)
)

if __name__ == "__main__":
    logging.basicConfig()
    run()