# Project C-WARN: AI-Powered Cloudburst Early Warning System

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![IoT](https://img.shields.io/badge/IoT-ESP32%20%26%20LoRaWAN-orange)

**C-WARN (Cloudburst Warning and Alert Response Network)** is an AI-powered IoT system designed to predict hyperlocal cloudbursts in mountainous regions, providing a critical 15-30 minute advance warning to save lives.

This project is the official submission for the **Smart India Hackathon 2025**, targeting problem statement **SIH25227**.

---

### Table of Contents
1.  [About The Project](#about-the-project)
2.  [Architecture](#architecture)
3.  [Built With](#built-with)
4.  [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
5.  [Usage](#usage)
6.  [Future Roadmap](#future-roadmap)
7.  [Contact](#contact)

---

## About The Project

![Project C-WARN Concept](https://i.imgur.com/eB9jJ4J.png) 
*(This is a placeholder for your "Digital Shield" infographic)*

Existing weather systems provide regional forecasts but lack the resolution to predict sudden, violent cloudbursts in a single valley. This "hyperlocal gap" leaves communities with no actionable warning against devastating flash floods.

Project C-WARN solves this by deploying a dense network of low-cost, autonomous IoT sensors that monitor the **atmospheric precursors** to a cloudburst (cloud temperature, pressure, and charge). Our key innovation is **Predictive Precursor Analysis**, where a spatio-temporal AI model analyzes these patterns to issue a life-saving alert **before** the rain begins.

---

## Architecture

The C-WARN system is a complete end-to-end data pipeline, structured in four key stages:

![C-WARN Technical Pipeline](https://i.imgur.com/your-pipeline-image.png)
*(This is a placeholder for your "Technical Approach" infographic)*

1.  **SENSE:** Autonomous "Megha-Drishti" nodes in the field collect real-time atmospheric data.
2.  **TRANSMIT:** Data is sent via a LoRaWAN network to an MQTT broker in the cloud.
3.  **ANALYZE:** A Python-based backend ingests the data, and our TensorFlow AI model analyzes it for cloudburst signatures.
4.  **ALERT:** A live command center dashboard and multi-channel alerts (Sirens, SMS, App) are triggered if a threat is detected.

---

## Built With

This project combines edge hardware with a modern cloud and web stack.

* **Hardware:**
    * ESP32 Microcontroller
    * LoRaWAN Communication Module (RA-02)
    * Sensor Suite (MLX90614, BME280, AS3935)
    * Solar Power System
* **Backend & AI:**
    * Python
    * Flask
    * TensorFlow
    * PostgreSQL + PostGIS
* **Communication:**
    * MQTT
* **Frontend:**
    * JavaScript
    * Leaflet.js
    * Chart.js & Canvas-Gauges
    * Kotlin (for the Android App)

---

## Getting Started

This guide will get you a local copy of the virtual prototype up and running.

### Prerequisites

You'll need Python 3.8+ and pip installed on your system.
* Python & pip
    ```sh
    python --version
    ```

### Installation

1.  **Clone the repo**
    ```sh
    git clone [https://github.com/your_username/project-cwarn.git](https://github.com/your_username/project-cwarn.git)
    cd project-cwarn
    ```
2.  **Create and activate a Python virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Python packages**
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

The virtual prototype simulates the hardware using Wokwi and runs the real backend and dashboard locally.

1.  **Run the Backend Server:**
    Open a terminal, activate the environment, and run the Flask app.
    ```sh
    python app.py
    ```
2.  **Run the Wokwi Simulation:**
    * Open the `project-cwarn.wokwi` project in a web browser.
    * Add your Wi-Fi credentials to the `sketch.ino` file.
    * Click "Start Simulation". The simulated ESP32 will connect to your Wi-Fi and start publishing data to the MQTT broker.
3.  **View the Dashboard:**
    Open your browser and navigate to `http://127.0.0.1:5000`. You should see the live dashboard receiving data from the Wokwi simulation.
4.  **Trigger an Alert:**
    To test the alert system, stop the Wokwi simulation, change the `TRIGGER_CLOUDBURST_EVENT` flag to `true` in `sketch.ino`, and restart the simulation.

---

## Future Roadmap

1.  **Phase 1 (1 Year):** Pilot Deployment of physical nodes in a high-risk valley and begin data collection.
2.  **Phase 2 (2 Years):** Use collected data to train and refine the spatio-temporal neural network.
3.  **Phase 3 (3 Years):** Scale the deployment to other vulnerable regions and integrate with the National Disaster Management Authority (NDMA).

---

## Contact

[Your Team Name] - [your-email@example.com]

Project Link: [https://github.com/your_username/project-cwarn](https://github.com/your_username/project-cwarn)
