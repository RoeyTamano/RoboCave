# 🤖 RoboCave

**RoboCave** is a project that involves a robotic vehicle equipped with sensors to measure air quality, distance, and other environmental parameters. The vehicle can be controlled remotely via a web interface, allowing it to move forward, backward, turn, and stop. 

## 🚀 Features

- **Real-time Sensor Data**: Measures temperature, humidity, pressure, LPG, CO, smoke levels, and distance.
- **Remote Control**: Control the robot's movements (forward, backward, left, right) via a web interface.
- **Web Interface**: A responsive HTML page that displays sensor readings and provides control buttons.
- **PWM Motor Control**: Uses PWM signals to control the speed of DC motors.

## 🛠️ Technologies Used

- **MicroPython**: Programming language used for the ESP32 microcontroller.
- **BME280**: Sensor library for measuring temperature, humidity, and pressure.
- **ADC**: Used to read analog values from gas sensors.
- **I2C**: Communication protocol for interfacing with sensors.
- **HTML/CSS/JavaScript**: For creating the web interface to interact with the robot.

## 📦 Installation

### Set up the Microcontroller:

1. Flash MicroPython onto your ESP32 board.
2. Install necessary libraries (like BME280) using `ampy` or another tool.

### Edit the Code:

- Update the Wi-Fi credentials in the code:
   ```python
   ssid = 'Your_SSID'
   password = 'Your_Password'
### Upload the Code:

- Upload the code to your ESP32.

### Run the Code:

- Open a terminal to view the output and ensure the server is running.

### Access the Web Interface:

- Open a web browser and enter the IP address of your ESP32 to access the control interface.

## 🌐 Usage

- **Control the Robot**: Use the buttons on the web interface to control the robot's movements.
- **View Sensor Data**: The interface will display real-time readings for temperature, humidity, pressure, and gas levels.



