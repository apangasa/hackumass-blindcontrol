from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)

# allow cross-origin resource sharing
CORS(app)

# requests will be routed to this endpoint when it is time for an instruction to be executed
LOCAL_ENDPOINT_URL = 'http://d45265a26389.ngrok.io'

MODE = 'automatic'
STATE = 'open'


# A way to quickly check if the endpoint has deployed properly
@app.route('/', methods=['GET'])
def helloWorld():
    return 'Blind Control Endpoint is up and running!', 200


# Returns the current mode (manual or automatic)
@app.route('/get-mode', methods=['GET'])
def getMode():
    global MODE
    return jsonify(mode=MODE), 200


# Returns the current dictionary schedule with keys being time and values being 'open' or 'closed'
@app.route('/get-schedule', methods=['GET'])
def getSchedule():
    with open('./schedule.json', 'r') as schedule_file:
        schedule = json.load(schedule_file)
        return jsonify(schedule), 200


# Sets the state (open or closed) based on a post request from the local endpoint
@app.route('/receive-state', methods=['POST'])
def receiveState():
    global STATE
    state = request.json.get('state', None)
    if not state:
        return 'No state provided', 400
    STATE = state
    return jsonify(success=True), 200


# Sends state to frontend app so the user knows the current state of their blinds at all times
@app.route('/get-state', methods=['GET'])
def getState():
    global STATE
    return jsonify(state=STATE), 200


# Flask app will get a request from the frontend client application
# Occurs when user presses button to change mode from manual to auto / vice versa
# This endpoint will simply route this change directly to the local endpoint
@app.route('/change-mode', methods=['POST'])
def changeMode():
    global MODE
    mode = request.json.get('mode', None)
    if not mode:
        return 'No mode specified', 400
    MODE = mode

    # The following code invokes the scheduler Cloud Function.
    # It is commented out because full functionality along the pipeline for this has not been completely implemented.
    # if mode == 'manual':
    #     schedule = {}
    #     with open('./schedule.json', 'r') as schedule_file:
    #         schedule = json.load(schedule_file)
    #           requests.post(
    #               'https://us-east1-blind-control-299118.cloudfunctions.net/scheduler', json=schedule)

    requests.post(LOCAL_ENDPOINT_URL + '/write-mode', json={'mode': mode})
    return jsonify(success=True), 200


# Flask app receives request to open or close the blinds
# This will happen only if mode is set to manual
# Otherwise, it will throw an error and continue in auto
@app.route('/flip', methods=['POST'])
def openClose():
    global MODE
    global STATE

    if MODE == 'automatic':
        return 'Switch to manual!', 400

    new_state = request.json.get('new_state', None)
    if not new_state:
        return 'No new state specified', 400
    requests.post(LOCAL_ENDPOINT_URL + '/flip', json={'new_state': new_state})
    STATE = new_state
    return jsonify(success=True), 200


# Dump the schedule dict {time: state} into a JSON file
@app.route('/set-schedule', methods=['POST'])
def setSchedule():
    schedule = request.json

    with open('./schedule.json', 'w') as schedule_file:
        json.dump(schedule, schedule_file)

    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run(debug=True)
