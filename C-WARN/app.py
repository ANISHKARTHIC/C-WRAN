# app.py

from flask import Flask, jsonify, render_template
from flask_cors import CORS
import paho.mqtt.client as mqtt
import json
import threading

# --- Configuration ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "sih/project_cwarn/data"

# --- Flask App Setup ---
app = Flask(__name__)
CORS(app) # Allow cross-origin requests

# --- Data Storage (In-memory for this prototype) ---
# This dictionary will hold the latest data received from the sensor
latest_data = {
    "node_id": "N/A",
    "status": "INITIALIZING",
    "pressure_hpa": 0,
    "sky_temp_c": 0,
    "charge_v": 0,
}
data_lock = threading.Lock()

# --- AI Logic (Simplified for Prototype) ---
def analyze_data(data):
    # This is a simple rule-based "AI" to determine the status
    pressure = data.get("pressure_hpa", 1012)
    charge = data.get("charge_v", 110)
    
    if pressure < 980 and charge > 800:
        return "ALERT"
    elif pressure < 1000 and charge > 500:
        return "WARNING"
    else:
        return "NORMAL"

# --- MQTT Client Setup ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Backend connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"❌ Failed to connect to backend, return code {rc}\n")

def on_message(client, userdata, msg):
    global latest_data
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        status = analyze_data(data)
        
        # Use a lock to prevent race conditions when updating the data
        with data_lock:
            latest_data = data
            latest_data["status"] = status
            
        print(f"Received and processed data: {latest_data}")
        
    except Exception as e:
        print(f"Error processing message: {e}")

# Setup and start the MQTT client in a separate thread
client = mqtt.Client(protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message
client.connect_async(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

# --- API Endpoints ---
@app.route('/')
def index():
    # Serve the main dashboard page
    return render_template('index.html')

@app.route('/api/latest_data')
def get_latest_data():
    # Provide the latest data to the frontend
    with data_lock:
        return jsonify(latest_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)