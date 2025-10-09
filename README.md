# C-WARN: Cloudbust Warning Alart Raising Network

C-WARN is a real-time vehicle monitoring and collision alert system. It features a web-based dashboard that displays a vehicle's live location, speed, and operational status on an interactive map. The system uses an MQTT messaging protocol for efficient, low-latency communication between a simulated vehicle sensor and the web server.

---

## Features 🗺️

* **Live Vehicle Tracking:** Displays the vehicle's current position on a map in real-time.
* **Real-time Data Display:** Shows live updates for speed, latitude, longitude, and system status.
* **Modular Architecture:** Decoupled sensor simulation and web interface using an MQTT broker.
* **Lightweight & Fast:** Built with Flask and MQTT for a responsive user experience.

---

## Tech Stack 🛠️

* **Backend:** Python, Flask
* **Real-time Messaging:** Paho-MQTT
* **CORS Handling:** Flask-CORS
* **Frontend:** HTML, CSS, JavaScript (with a mapping library like Leaflet.js)

---

## How It Works

The system consists of three main components:

1.  **Sensor Simulator (`sensor_simulator.py`):** This script acts as a virtual vehicle. It generates random location and speed data and **publishes** it to an MQTT topic.
2.  **MQTT Broker:** A message broker (like Mosquitto) receives the data from the simulator and forwards it to any subscribed clients. **You must have an MQTT broker running for this application to work.**
3.  **Flask Web Application (`app.py`):** The backend server **subscribes** to the MQTT topic. It receives the live data, processes it, and serves it to the frontend. The web dashboard then visualizes this data.

---

## Getting Started 🚀

Follow these instructions to get the project running on your local machine.

### Prerequisites

* Python 3.7+
* An MQTT Broker (e.g., [Mosquitto](https://mosquitto.org/download/)) installed and running.

### Installation & Setup

1.  **Clone the repository** (if applicable)
    ```bash
    git clone <your-repository-url>
    cd C-WARN
    ```

2.  **Create and activate a Python virtual environment**
    * On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies**
    ```bash
    pip install flask paho-mqtt flask-cors
    ```
    *(Note: It's good practice to have these in a `requirements.txt` file and run `pip install -r requirements.txt`)*

### Running the Application

You will need to open **two separate terminals** for this process.

1.  **Terminal 1: Run the Sensor Simulator**
    Make sure your virtual environment is activated and your MQTT broker is running.
    ```bash
    python sensor_simulator.py
    ```
    This will start sending vehicle data to your broker.

2.  **Terminal 2: Run the Flask Web Server**
    Open a new terminal and activate the virtual environment again.
    ```bash
    python app.py
    ```

3.  **View the Dashboard**
    Open your favorite web browser and navigate to:
    **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## Screenshots

Here is a preview of the C-WARN dashboard in action.

![C-WARN Dashboard showing a map with a vehicle location and data panels](MEDIA/image.png)
