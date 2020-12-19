from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)

# allow cross-origin resource sharing
CORS(app)

# requests will be routed to this endpoint when it is time for an instruction to be executed
LOCAL_ENDPOINT_URL = ''

# A way to quickly check if the endpoint has deployed properly


@app.route('/', methods=['GET'])
def helloWorld():
    return 'Blind Control Endpoint is up and running!', 200


# Flask app will get a request from the frontend client application
# Occurs when user presses button to change mode from manual to auto / vice versa
# This endpoint will simply route this change directly to the local endpoint
@app.route('/change-mode', methods=['POST'])
def changeMode():
    mode = request.json.get('mode', None)
    if not mode:
        return 'No mode specified', 400

    if mode == 'manual':
        schedule = {}
        with open('./schedule.json', 'r') as schedule_file:
            schedule = json.load(schedule_file)
        # run cloud function

    with open('./mode.data', 'w') as mode_file:
        mode_file.write(mode)

    requests.post(LOCAL_ENDPOINT_URL + '/write-mode', json={'mode': mode})
    return jsonify(success=True), 200


# Flask app receives request to open or close the blinds
# This will happen only if mode is set to manual
# Otherwise, it will throw an error and continue in auto
@app.route('/flip', methods=['POST'])
def openClose():
    new_state = request.json.get('new_state', None)
    if not new_state:
        return 'No new state specified', 400
    requests.post(LOCAL_ENDPOINT_URL + '/flip', json={'new_state': new_state})
    return jsonify(success=True), 200


@app.route('/set-schedule', methods=['POST'])
def setSchedule():
    schedule = request.json

    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run(debug=True)
