# Android Sensor Data Collection System

A web-based system for collecting sensor data and camera frames from Android devices using WebXR and WebSockets. The system includes text-to-speech capabilities and ZMQ-based data distribution.

## Features
- Real-time AR pose tracking using WebXR
- Camera frame capture and streaming using front(user) camera
- Text-to-speech feedback system
- Secure WebSocket communication
- ZMQ-based data publishing for low latency

## Prerequisites

- Node.js >= 14.x
- SSL certificates (`cert.pem` and `key.pem`)
- Compatible Android device with WebXR support
- Modern web browser with WebXR support

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/android-xr-sensor-bridge.git
cd android-xr-sensor-bridge
```
2. Install dependencies:
```bash
npm install
```

3. Set up SSL certificates in the root directory:
    - Generate or place your SSL certificates:
        - `cert.pem` - SSL certificate
        - `key.pem` - Private key

## Usage
1. Start the server:

```bash
node server.js
```

2. Access the web interface:
   - Open `https://localhost:4004` on your Android device
   - Accept camera and AR permissions when prompted
   - Click "Start" to begin data collection


## Data Format

The system transmits data in the following JSON format:

```json
{
  "timestamp": 1234567890,
  "pose": {
    "position": {"x": 0.0, "y": 0.0, "z": 0.0},
    "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}
  },
  "camera": "base64_encoded_jpeg"
}
```

### Testing
Test the data flow using receiver.py:
```bash
python3 test/receiver.py
```

and TTS using:
```bash
python3 test/tts_sender.py
```

## Troubleshooting

- Ensure SSL certificates are valid
- Check if ports 4000, 5556, and 5557 are available
- Verify Android device supports WebXR

## Contributing

I'm actively seeking community support to enhance this project's efficiency and expand its capabilities. If you're interested in contributing, whether it's through optimizing the real-time data processing, adding new sensor capabilities, or improving documentation, your help would be greatly appreciated.