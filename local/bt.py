import serial
from serial import Serial
import time
arduino = serial.Serial(port='COM12', baudrate=9600, timeout=None)

def main():
    # arduino.write(bytes(x, 'utf-8'))
    while True:
        data = arduino.read(1)
        print(data)

if __name__ == "__main__":
    main()