import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
socket.subscribe("pose")  # Subscribe to 'pose' topic

while True:
    topic = socket.recv_string()
    msg = socket.recv_string()
    data = json.loads(msg)
    print(f"Position: {data['position']}")
    print(f"Orientation: {data['orientation']}")