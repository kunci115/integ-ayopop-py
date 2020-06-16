from flask import Flask, Response
import json
from socket_client import tcp_handler
from flask import request, jsonify
app = Flask(__name__)


@app.route('/payment-callback', methods=['POST'])
def idm_api():
    if request.method == 'POST':
        data = request.json
        tcp_handler(data)
        return Response("200")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3333)
