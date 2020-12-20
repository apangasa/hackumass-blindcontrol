from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

WORKDIR = '.'  # The directory of the local filesystem where workfiles should be read from and written to


# A way to quickly check if the endpoint has deployed properly
@app.route('/', methods=['GET'])
def helloWorld():
    return 'Local Endpoint is up and running!', 200


# This Flask app will receive a post request from the cloud endpoint
# Occurs after the user specifies to change the mode
# This will be written to the local filesystem to be read by the local script
@app.route('/write-mode', methods=['POST'])
def writeMode():
    mode = request.json.get('mode', None)
    if not mode:
        return 'No mode specified', 400

    with open(WORKDIR + '/mode.data', 'w') as mode_file:
        mode_file.write('0' if mode == 'manual' else '1')

    return jsonify(success=True), 200


# This is triggered when the blinds need to be in a specific state
# This may occur due to a scheduled post request that the client set up
# It may also occur due to a direct request by the client
# The new state is written to the instruction queue to be read by the local script
@app.route('/flip', methods=['POST'])
def openClose():
    new_state = request.json.get('new_state', None)
    if not new_state:
        return 'No state specified', 400

    with open(WORKDIR + '/instructions.data', 'w') as instructions:
        instructions.write('0' if new_state == 'closed' else '1')

    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run()
