from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)

# allow cross-origin resource sharing
CORS(app)

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
    local_endpoint_url = ''
    requests.post(local_endpoint_url + '/write-mode', json={'mode': mode})
    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run()
