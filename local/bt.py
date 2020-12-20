import serial, requests
import time
#get arduino communication setup from port COM12
arduino = serial.Serial(port='COM12', baudrate=9600, timeout=None)

def main():
    #start sending and recieving data
    while True:
        instr = None
        mode = None
        #if instruction (open/close) perfom action if right mode
        with open('./instructions.data', 'r') as instructions:
            instr = instructions.read()
        #get mode if user sends mode change (automatic/manual)
        with open('./mode.data', 'r') as modes:
            mode = modes.read()
        #get blind state from arduino
        state = arduino.read(1)
        #send current state to cloud
        sendToCloud(state)
        if mode == '1':
            #if in automatic mode, no instructions
            arduino.write(bytes('2', 'ascii'))
        else:
            #if in manual mode send latest instruction
            arduino.write(bytes(instr[-1], 'ascii'))

def sendToCloud(state):
    #send information on blind state over cloud
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
    #wait 3 seconds before starting to setup communications
    time.sleep(3)
    main()
