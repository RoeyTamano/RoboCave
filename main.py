import usocket as socket
import network
import time
from machine import PWM, Pin, ADC, I2C, time_pulse_us
import gc
import BME280
import json
from dc_motor import DCMotor

gc.collect()

TRIG_PIN = 25
ECHO_PIN = 35

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

a2 = PWM(Pin(26), duty=0)
a1 = PWM(Pin(27), freq=500, duty=0)
b2 = PWM(Pin(22), duty=0)
b1 = PWM(Pin(23), duty=0)
adc = ADC(Pin(34))

ssid = 'POCO M5'
password = '20304050'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

frequency = 15000       
pin1 = Pin(5, Pin.OUT)    
pin2 = Pin(4, Pin.OUT)
pin3 = Pin(18, Pin.OUT)    
pin4 = Pin(19, Pin.OUT)
enable1 = PWM(Pin(13), frequency)
enable2 = PWM(Pin(12), frequency)
dc_motor1 = DCMotor(pin1, pin2, enable1, 350, 1023)
dc_motor2 = DCMotor(pin3, pin4, enable2, 350, 1023)
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print("Connecting", end="")
while not station.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("Connection successful")
print("System parameters: ", station.ifconfig())

def web_page():
    html = """<html>
<head>
    <title>WLAN server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }
        body {
            background: linear-gradient(90deg, rgba(55,46,191,1) 0%, rgba(63,198,224,1) 100%);
        }
        div {
            display: inline-block;
            border: solid;
            border-radius: 30px;
            margin: 10px;
            padding: 10px;
            background-color: #32c3ba;
        }
        h1 {
            color: black;
            padding: 2vh;
            font-size: 20px;
        }
        button {
            border-radius: 30px;
            padding: 20px;
        }
        .buttonGreen, .buttonRed, .buttonBlue, .buttonYellow, .buttonGray, .buttonDblue {
            display: inline-block;
            background-color: #32c3ba;
            border: none;
            font-size: 20px;
            margin: 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1 style="font-size:50px;">RoboCave</h1>
    <div id="air-condition">
        <h2>Measuring the air condition</h2>
        <p>Temperature: <span id="temperature">--</span></p>
        <p>Humidity: <span id="humidity">--</span></p>
        <p>Pressure: <span id="pressure">--</span></p>
    </div>
    <div id="gas-condition">
        <h2>Measuring the gas condition</h2>
        <p>LPG: <span id="lpg">--</span> ppm</p>
        <p>CO: <span id="co">--</span> ppm</p>
        <p>SMOKE: <span id="smoke">--</span> %</p>
    </div>
    <div id="distance">
        <h2>Measuring the distance</h2>
        <p>Distance: <span id="distance-value">--</span> cm</p>
    </div>
    <p>
        <a href="/gass"><button class="buttonBlue"><strong>gass</strong></button></a>
    </p>
    <p>
        <a href="/left"><button class="buttonGreen"><strong>left</strong></button></a>
        <a href="/slow"><button class="buttonGray"><strong>slow</strong></button></a>
        <a href="/right"><button class="buttonRed"><strong>right</strong></button></a>
    </p>
    <p>
        <a href="/stop"><button class="buttonGray"><strong>stop</strong></button></a>
        <a href="/back"><button class="buttonYellow"><strong>back</strong></button></a>
        <a href="/180"><button class="buttonDblue"><strong>180</strong></button></a>
    </p>
    <audio controls autoplay>
        <source src="/audio" type="audio/wav">
        Your browser does not support the audio element.
    </audio>

    <script>
        function fetchData() {
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('temperature').innerText = data.temperature;
                    document.getElementById('humidity').innerText = data.humidity;
                    document.getElementById('pressure').innerText = data.pressure;
                    document.getElementById('lpg').innerText = data.lpg.toFixed(2);
                    document.getElementById('co').innerText = data.co.toFixed(2);
                    document.getElementById('smoke').innerText = data.smoke.toFixed(2);
                    document.getElementById('distance-value').innerText = data.distance.toFixed(2); // עדכון המרחק
                })
                .catch(error => console.error('Error fetching data:', error));
        }

        setInterval(fetchData, 1000);
    </script>
</body>
</html>
"""
    return html

def adc_to_ppm(adc_value, gas_type):
    calibration_factors = {'lpg': 0.3, 'co': 0.4, 'smoke': 0.2}
    return (4095 - adc_value) * calibration_factors[gas_type] / 4095

def measure_distance():
    trig.off()
    time.sleep_us(2)

    trig.on()
    time.sleep_us(10)
    trig.off()

    duration = time_pulse_us(echo, 1, 30000)  

    if duration < 0:
        print("Error: Echo pulse duration is out of range")
        return None

    distance = (duration / 2) / 29.1 
    return distance

def forward(x):
    dc_motor1.forward(100)
    dc_motor2.forward(100)
    time.sleep(0.1)
    print("gass", x)
    return x

def slow(x):
    dc_motor1.forward(50)
    dc_motor2.forward(50)
    time.sleep(0.1)

def back(r):
    dc_motor1.backwards(100)
    dc_motor2.backwards(100)
    time.sleep(0.1)
    print("back", r)
    return r

def turn_l(x):
    dc_motor1.forward(100)
    dc_motor2.forward(50)
    print("right", x)

def turn_r(x):
    dc_motor2.forward(100)
    dc_motor1.forward(50)
    print("left", x)

def turn_180(x):
    dc_motor1.forward(100)
    dc_motor2.backwards(100)
    print("t180", x)

def get_sensor_data():
    lpg = adc.read()
    co = adc.read()
    smoke = adc.read()

    lpg_ppm = adc_to_ppm(lpg, 'lpg')
    co_ppm = adc_to_ppm(co, 'co')
    smoke_ppm = adc_to_ppm(smoke, 'smoke')

    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure

    distance = measure_distance()
    if distance is None:
        distance = 0.0

    return {
        'temperature': temp,
        'humidity': hum,
        'pressure': pres,
        'lpg': lpg_ppm,
        'co': co_ppm,
        'smoke': smoke_ppm,
        'distance': distance
    }

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    
    if 'GET /data' in request:
        sensor_data = get_sensor_data()
        response = json.dumps(sensor_data)
        conn.send('HTTP/1.1 200 OK\nContent-Type: application/json\nConnection: close\n\n')
        conn.sendall(response)
    else:
        if '/gass' in request:
            forward(1)
        if '/back' in request:
            back(1)
        if '/left' in request:
            turn_l(1)
        if '/right' in request:
            turn_r(1)
        if '/stop' in request:
            dc_motor1.stop()
            dc_motor2.stop()
        if '/180' in request:
            turn_180(1)
        if '/slow' in request:
            slow(1)

        response = web_page()
        conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
        conn.sendall(response)
    conn.close()