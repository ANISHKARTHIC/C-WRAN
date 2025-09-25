
import json
import time
import random
import paho.mqtt.client as mqtt

# --- Configuration ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "sih/project_cwarn/data"
NODE_ID = "MD-01"
SIMULATION_SPEED_SECONDS = 3 # Send data every 3 seconds

# --- Cloudburst Event Trigger ---
# To trigger an event, change this to True and restart the script
TRIGGER_CLOUDBURST_EVENT = True

# --- MQTT Setup ---
# Using MQTTv311 for broader compatibility with public brokers
client = mqtt.Client(client_id=f"sensor-{NODE_ID}", protocol=mqtt.MQTTv311, transport="tcp")
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("✅ Connected to MQTT Broker!")
except Exception as e:
    print(f"❌ Failed to connect to MQTT Broker: {e}")
    exit()

client.loop_start()

# --- Main Simulation Loop ---
print(f"▶️ Starting sensor simulation for Node ID: {NODE_ID}")
print(f"▶️ Cloudburst Event Trigger is set to: {TRIGGER_CLOUDBURST_EVENT}")

while True:
    if TRIGGER_CLOUDBURST_EVENT:
        # Generate data that looks like a cloudburst event
        pressure = 950.5 + random.uniform(-1, 1)    # Sharp pressure drop
        sky_temp = -15.2 + random.uniform(-1, 1)   # Sharp temperature drop
        charge = 850.0 + random.uniform(-5, 5)     # High atmospheric charge
    else:
        # Generate normal weather data
        pressure = 1012.3 + random.uniform(-1, 1)
        sky_temp = 12.5 + random.uniform(-1, 1)
        charge = 110.0 + random.uniform(-5, 5)

    # Create the data payload as a dictionary
    data = {
        "node_id": NODE_ID,
        "pressure_hpa": round(pressure, 2),
        "sky_temp_c": round(sky_temp, 2),
        "charge_v": round(charge, 2),
        "timestamp": time.time()
    }

    # Convert dictionary to JSON string
    payload = json.dumps(data)

    # Publish the data to the MQTT topic
    result = client.publish(MQTT_TOPIC, payload)
    status = result[0]
    if status == 0:
        print(f"Sent `{payload}` to topic `{MQTT_TOPIC}`")
    else:
        print(f"❌ Failed to send message to topic {MQTT_TOPIC}")

    time.sleep(SIMULATION_SPEED_SECONDS)