# 🤖 RoboCave Project

## Overview
The RoboCave project is designed to create a robotic vehicle capable of gathering and transmitting information about environmental conditions 🌍, including air quality and distance measurements. The robot can be controlled via a web interface 🖥️, providing real-time data and control options.

## Hardware Components
- **Microcontroller**: ESP32 or similar microcontroller.
- **Sensors**:
  - **BME280**: Measures temperature 🌡️, humidity 💧, and atmospheric pressure 🌬️.
  - **Gas Sensors**: 
    - LPG sensor (analog output).
    - CO sensor (analog output).
    - Smoke sensor (analog output).
  - **Ultrasonic Distance Sensor**: Used to measure distance 📏.
- **DC Motors**: Two DC motors for movement control 🏎️.
- **Motor Driver**: H-Bridge motor driver for controlling the direction and speed of the motors.
- **PWM Pins**: For controlling motor speed via Pulse Width Modulation.
- **Connection Pins**: GPIO pins for connecting sensors and motors.

### ❗The picture doesn't show what the robot looks like now, it's an old picture from when it didn't have all the sensors and the design is different without a cover for the robot.
![image](https://github.com/user-attachments/assets/85004705-0c19-4549-bb4c-184152e27d57) 


## Software Components
- **MicroPython**: The firmware running on the microcontroller.
- **Libraries**:
  - `usocket`: For socket communication 🔌.
  - `network`: For connecting to Wi-Fi 📶.
  - `machine`: For controlling hardware components ⚙️.
  - `BME280`: For interfacing with the BME280 sensor.
  - `json`: For handling JSON data.

## Features
- **Web Interface**: 
  - Displays real-time sensor data (temperature, humidity, pressure, gas concentrations, and distance).
  - Provides control buttons for motor actions (forward, backward, left, right, stop) 🚦.

  ![image](https://github.com/user-attachments/assets/3a755f92-2872-4b72-9903-8553e4b103b5)

- **Data Fetching**: JavaScript is used to periodically fetch sensor data from the server and update the webpage without refreshing 🔄.
- **Distance Measurement**: The robot can measure the distance to obstacles using an ultrasonic sensor 📏.

## Usage
1. **Setup**: Connect the hardware components as specified in the circuit diagram 🔌.
2. **Code Deployment**: Upload the provided MicroPython script to the microcontroller 📤.
3. **Wi-Fi Configuration**: Update the SSID and password in the code for your Wi-Fi network 🔑.
4. **Accessing the Web Interface**: 
   - Once connected to Wi-Fi, open a web browser and navigate to the microcontroller's IP address to access the control interface 🌐.
5. **Controlling the Robot**: Use the buttons on the web interface to control the robot's movement and monitor environmental conditions 🎮.

## Getting Started
1. Clone this repository or download the code files 📥.
2. Download Thoney micropython
3. Flash the MicroPython firmware onto your ESP32 💻.
4. Install the necessary libraries (if not included in the firmware).
5. Connect your ESP32 to your computer and upload the script ⬆️.
6. Open the web interface and begin monitoring and controlling the RoboCave 🚀.

## Conclusion
The RoboCave project combines hardware and software to create a functional robot capable of navigating and monitoring environmental conditions 🛰️. This project serves as a foundation for further enhancements, such as adding more sensors, improving user interface design, and enhancing the robot's navigation capabilities.


