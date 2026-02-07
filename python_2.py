
import serial
import time
from pynput.keyboard import Controller

SERIAL_PORT = "COM6"    
BAUD_RATE = 115200

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0)
time.sleep(2)

keyboard = Controller()

speed_key = None
steer_key = None

def release(key):
    if key:
        keyboard.release(key)

print("Dual-joystick")

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            if not line:
                continue

          
            parts = line.split()
            if len(parts) != 2:
                continue

            speed_cmd = parts[0].split(":")[1]
            steer_cmd = parts[1].split(":")[1]

     
            release(speed_key)
            speed_key = None

            if speed_cmd == "F":
                 speed_key = 'w'
            elif speed_cmd == "B":
                speed_key = 's'

            if speed_key:
                keyboard.press(speed_key)

            release(steer_key)
            steer_key = None
            if steer_cmd == "L":
                steer_key = 'a'
            elif steer_cmd == "R":
                steer_key = 'd'

            if steer_key:
                keyboard.press(steer_key)

except KeyboardInterrupt:
    release(speed_key)
    release(steer_key)
    print("Stopped")