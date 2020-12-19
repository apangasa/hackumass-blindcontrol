from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def helloWorld():
    return 'Blind Control Endpoint is up and running!', 200


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
