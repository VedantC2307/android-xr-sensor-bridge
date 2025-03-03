import zmq
import time

def main():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5557")
    print("TTS Publisher bound to port 5557")

    time.sleep(5)

    try:
        while True:
            # Example: Send a test message every 5 seconds
            message = """Hello, this is a test message. How are you doing. 
            I am just checking how long you can listen to me or speak to me. This ensures TTS only starts when the AR session begins and properly cleans up when it ends.
            I'll help modify the index.html to only start TTS when the button is clicked. Here are the changes needed:"""
            publisher.send_multipart([b"tts", message.encode()])
            print(f"Sent TTS message: {message}")
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        publisher.close()
        context.term()

if __name__ == "__main__":
      # Wait for ZMQ publisher to bind
    main()
