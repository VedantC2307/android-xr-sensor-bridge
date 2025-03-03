import zmq
import json
import base64
import numpy as np
import cv2
from datetime import datetime
import os

def main():
    # Create images directory if it doesn't exist
    image_dir = 'captured_images'
    os.makedirs(image_dir, exist_ok=True)
    
    # Initialize ZMQ subscriber
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.subscribe("sensor_data")
    print("Connected to ZMQ publisher")
    print(f"Images will be saved to: {os.path.abspath(image_dir)}")

    try:
        while True:
            topic = socket.recv_string()
            message = socket.recv_string()
            data = json.loads(message)
            
            timestamp = datetime.fromtimestamp(data['timestamp']/1000.0)
            
            # Process pose data
            pose = data['pose']
            position = pose['position']
            orientation = pose['orientation']
            
            print(f"\nTimestamp: {timestamp}")
            print(f"Position: x={position['x']:.3f}, y={position['y']:.3f}, z={position['z']:.3f}")
            print(f"Orientation: x={orientation['x']:.3f}, y={orientation['y']:.3f}, z={orientation['z']:.3f}, w={orientation['w']:.3f}")
            
            # Save camera frame if available
            if data['camera']:
                # Convert base64 string to image
                img_bytes = base64.b64decode(data['camera'])
                img_arr = np.frombuffer(img_bytes, np.uint8)
                img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
                
                # Generate filename with timestamp
                filename = os.path.join(image_dir, f"frame_{timestamp.strftime('%Y%m%d_%H%M%S_%f')}.jpg")
                cv2.imwrite(filename, img)
                print(f"Saved image: {filename}")

    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    main()
