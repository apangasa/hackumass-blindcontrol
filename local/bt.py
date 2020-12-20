import serial, requests
import time
arduino = serial.Serial(port='COM12', baudrate=9600, timeout=None)

def main():
    while True:
        instr = None
        mode = None
        with open('./instructions.data') as instructions:
            instr = instructions.read()
        with open('./mode.data') as modes:
            mode = modes.read()
        state = arduino.read(1)
        print(state)
        print(instr)
        sendToCloud(state)
        if mode == '1':
            arduino.write(bytes('2', 'ascii'))
        else:
            arduino.write(bytes(instr, 'ascii'))

def sendToCloud(state):
    if not state:
        return
    url = 'https://blind-control-299118.ue.r.appspot.com/receive-state'
    blindState = None
    if state == b'1':
        blindState = {'state': "open"}
    else:
        blindState = {'state': "closed"}

    requests.post(url, json = blindState)
    print(blindState)
    

if __name__ == "__main__":
    time.sleep(3)
    main()