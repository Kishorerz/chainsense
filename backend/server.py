from flask import Flask, jsonify, request
from web3 import Web3
import hashlib
import time
from flask import Flask, render_template, request, jsonify
import os

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'web_ui', 'static'),
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'web_ui', 'templates')
)

from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='../web_ui', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Existing routes...


# Connect to local Ganache blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
contract_address = '0x88925D6b81244179F0B1256D6A145f5173dE2d70'

# ABI Dictionary (trimmed to the relevant "abis" portion)
abi_dict = {
    "abis": {
        "0x3eed3ac93286cc807e961db2ce07426c4042f4cb422c3b072dea96b53fd0d53e": [
            {
                "inputs": [{"internalType": "string", "name": "_hash", "type": "string"}],
                "name": "addLog",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [{"internalType": "uint256", "name": "_index", "type": "uint256"}],
                "name": "getLog",
                "outputs": [
                    {"internalType": "string", "name": "", "type": "string"},
                    {"internalType": "uint256", "name": "", "type": "uint256"}
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "getTotalLogs",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "name": "logs",
                "outputs": [
                    {"internalType": "string", "name": "dataHash", "type": "string"},
                    {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
                ],
                "stateMutability": "view",
                "type": "function"
            }
        ]
    }
}

# Extract the correct ABI
contract_abi = abi_dict["abis"]["0x3eed3ac93286cc807e961db2ce07426c4042f4cb422c3b072dea96b53fd0d53e"]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
account = w3.eth.accounts[0]

# Simulated sensor data
current_temp = 31.4

@app.route("/temp")
def get_temp():
    return jsonify({"temp": current_temp})

@app.route("/logs")
def get_logs():
    logs = []
    total = contract.functions.getTotalLogs().call()
    for i in range(total):
        h, ts = contract.functions.getLog(i).call()
        logs.append({"hash": h, "timestamp": time.ctime(ts)})
    return jsonify(logs)

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json["data"]
    h = hashlib.sha256(data.encode()).hexdigest()
    total = contract.functions.getTotalLogs().call()
    match = any(contract.functions.getLog(i).call()[0] == h for i in range(total))
    return jsonify({"match": match})

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return send_from_directory('web_ui/build', 'index.html')

@app.route("/")
def serve_index():
    return send_from_directory("../web_ui", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("../web_ui", path)
@app.route('/')
def index():
    return render_template('index.html')
print("Total logs:", contract.functions.getTotalLogs().call())
