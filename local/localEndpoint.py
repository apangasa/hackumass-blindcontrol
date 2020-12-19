from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

WORKDIR = ''


@app.route('/', methods=['GET'])
def helloWorld():
    return 'Local Endpoint is up and running!', 200


@app.route('/write-mode', methods=['POST'])
def writeMode():
    mode = request.json.get('mode', None)
    if not mode:
        return 'No mode specified', 400

    with open(WORKDIR + '/mode.data', 'w') as mode_file:
        mode_file.write(mode)

    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run()
